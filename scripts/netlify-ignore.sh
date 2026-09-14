#!/usr/bin/env bash
# Netlify "ignore" command: decides whether a commit deploys.
#   exit 0 = skip the build   exit 1 = build
#
# Policy comes from DEPLOY_POLICY, set in the Netlify UI (Site configuration ->
# Environment variables). Deliberately NOT declared in netlify.toml, so the
# policy can change without a commit.
#
#   unset / "manual"  Deploy only when the commit message contains [deploy].
#   "auto"            Deploy everything except commits containing [skip build].
#
# Failure mode is deliberate: if the commit message cannot be determined, this
# BUILDS. A wasted build is recoverable; a gate that silently holds every commit
# forever is not.

set -uo pipefail

policy="${DEPLOY_POLICY:-manual}"
ref="${COMMIT_REF:-HEAD}"

# Try several ways to read the commit message; Netlify's checkout is shallow and
# the ref is not always reachable.
msg=""
for attempt in \
  "git log -1 --pretty=%B $ref" \
  "git log -1 --pretty=%B" \
  "git show -s --format=%B $ref" \
  "git show -s --format=%B"
do
  msg="$($attempt 2>/dev/null)" || true
  [ -n "${msg//[[:space:]]/}" ] && break
done

echo "netlify-ignore: policy=${policy} ref=${ref}"
echo "netlify-ignore: commit message read as:"
echo "---8<---"
echo "$msg"
echo "--->8---"

if [ -z "${msg//[[:space:]]/}" ]; then
  echo "netlify-ignore: could not read the commit message, building to be safe"
  exit 1
fi

# An explicit skip wins under either policy.
if printf '%s' "$msg" | grep -qiF '[skip build]'; then
  echo "netlify-ignore: marked [skip build], holding"
  exit 0
fi

if [ "$policy" = "auto" ]; then
  echo "netlify-ignore: auto policy, deploying"
  exit 1
fi

if printf '%s' "$msg" | grep -qiF '[deploy]'; then
  echo "netlify-ignore: marked [deploy], deploying"
  exit 1
fi

echo "netlify-ignore: manual policy and no [deploy] marker, holding this commit"
exit 0
