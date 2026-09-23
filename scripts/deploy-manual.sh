#!/usr/bin/env bash
#
# Publish the site by uploading a locally built copy, which consumes no Netlify
# credits because Netlify never runs a build. The plan allows 300 credits a
# month, about twenty builds, and they do not roll over.
#
#   scripts/deploy-manual.sh [--dry-run]
#
# Needs a Netlify personal access token in ~/.netlify-token, and the same Hugo
# version Netlify pins in netlify.toml.
#
# Read scripts/README-deploy.md before changing the build flags. They are
# copied from netlify.toml and a mismatch publishes a subtly different site.

set -euo pipefail

DRY_RUN=0
[ "${1:-}" = "--dry-run" ] && DRY_RUN=1

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_ID="6d02b1d0-aca7-48d5-8696-8bd877f9817c"
TOKEN_FILE="$HOME/.netlify-token"
BASE_URL="https://hxi.ucsd.edu"

die() { printf '\n  STOP: %s\n\n' "$*" >&2; exit 1; }
ok()  { printf '  ok    %s\n' "$*"; }

[ -f "$TOKEN_FILE" ] || die "no token at $TOKEN_FILE. Create one at
       https://app.netlify.com/user/applications#personal-access-tokens
       then: printf '%s' 'TOKEN' > $TOKEN_FILE && chmod 600 $TOKEN_FILE"

command -v hugo >/dev/null || die "hugo is not installed"
command -v python3 >/dev/null || die "python3 is not installed"

# Hugo version must match what Netlify pins, or the build can differ.
want="$(grep -E '^\s*HUGO_VERSION' "$REPO/netlify.toml" | tr -d ' "' | cut -d= -f2)"
have="$(hugo version | grep -oE 'v[0-9]+\.[0-9]+\.[0-9]+' | head -1 | tr -d v)"
[ "$want" = "$have" ] || die "hugo $have installed, netlify.toml pins $want"
ok "hugo $have matches netlify.toml"

cd "$REPO"

# Project author lists are derived from the publications attached to each project.
# Checked before the clean-tree test, so the fix can be reviewed and committed in
# the same pass rather than landing as an uncommitted edit mid-deploy.
python3 "$REPO/scripts/sync-project-authors.py" --check \
  || die "project pages are missing lab members who appear on their publications.
       Run the command above, review the diff, and commit."
ok "project authors match the publications"

# Deploy only what is committed, so the live site maps to a known commit.
[ -z "$(git status --porcelain)" ] || die "working tree is dirty. Commit first, so
       the deploy corresponds to a commit you can point at later:
$(git status --porcelain | sed 's/^/         /')"
HEAD_SHA="$(git rev-parse --short HEAD)"
ok "working tree clean at $HEAD_SHA"

[ -d .git ] || die "no .git here, and netlify.toml sets HUGO_ENABLEGITINFO=true"

echo
echo "  building (flags copied from netlify.toml)"
rm -rf public
HUGO_ENV=production HUGO_ENABLEGITINFO=true \
  hugo --gc --minify --buildFuture -b "$BASE_URL" >/dev/null
ok "built $(find public -type f | wc -l | tr -d ' ') files"

# Checks for the ways a local build silently differs from a Netlify one.
[ -f public/index.html ] || die "no public/index.html"
grep -q "$BASE_URL" public/index.html || die "base URL missing from the home page"
ok "base URL is $BASE_URL"

# netlify.toml is invisible to a manual deploy, so its rewrites have to come out
# of layouts/index.redirects instead. Anything only in netlify.toml 404s live.
want_rules=$(grep -cE '^\s*from = ' netlify.toml || true)
have_rules=$(grep -cE '^/' public/_redirects || true)
ok "_redirects carries $have_rules rules (netlify.toml declares $want_rules)"
for path in /weibel /weibel/cv /publications; do
  grep -qE "^$path " public/_redirects \
    || die "$path is in netlify.toml but not in public/_redirects.
       A manual deploy would 404 it. Add it to layouts/index.redirects."
done
ok "netlify.toml rewrites are present in _redirects"

if [ "$DRY_RUN" = 1 ]; then
  echo
  echo "  dry run, nothing uploaded. public/ is built and checked."
  exit 0
fi

echo
echo "  uploading"
SITE_ID="$SITE_ID" TOKEN_FILE="$TOKEN_FILE" python3 "$REPO/scripts/netlify-upload.py" "$REPO/public"

echo
echo "  live checks"
for path in / /weibel/cv /project/icontour/; do
  code=$(curl -s -o /dev/null -w '%{http_code}' -L --max-time 30 "$BASE_URL$path")
  printf '  %-4s %s\n' "$code" "$path"
done
echo
echo "  published $HEAD_SHA. Credits used: none (no build ran on Netlify)."
