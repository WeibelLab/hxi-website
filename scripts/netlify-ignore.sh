#!/usr/bin/env bash
# Netlify "ignore" command: decides whether a commit deploys.
#   exit 0 = skip the build   exit 1 = build
#
# Policy is set by the DEPLOY_POLICY environment variable in the Netlify UI
# (Site configuration -> Environment variables). Deliberately NOT set in
# netlify.toml, so the policy can be changed without a commit.
#
#   unset / "manual"  Nothing deploys unless the commit says [deploy].
#                     Use while the credit budget is tight (300/month plan).
#   "auto"            Everything deploys except commits saying [skip build].
#                     Use once the open source plan (10,000 credits) is active.
#
# A deploy can always be fired by hand, regardless of policy, from the Netlify
# UI or a build hook. Build hooks bypass this script entirely.

set -uo pipefail

msg="$(git log -1 --pretty=%B "${COMMIT_REF:-HEAD}" 2>/dev/null || git log -1 --pretty=%B)"
policy="${DEPLOY_POLICY:-manual}"

echo "netlify-ignore: policy=${policy}"

# An explicit skip wins under either policy.
if printf '%s' "$msg" | grep -qiF '[skip build]'; then
  echo "netlify-ignore: commit marked [skip build], not deploying"
  exit 0
fi

if [ "$policy" = "auto" ]; then
  echo "netlify-ignore: auto policy, deploying"
  exit 1
fi

if printf '%s' "$msg" | grep -qiF '[deploy]'; then
  echo "netlify-ignore: commit marked [deploy], deploying"
  exit 1
fi

echo "netlify-ignore: manual policy and no [deploy] marker, holding this commit"
exit 0
