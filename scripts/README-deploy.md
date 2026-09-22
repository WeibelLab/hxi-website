# Publishing

Two ways to publish, and the difference is where Hugo runs.

| | Git deploy | Manual deploy |
|---|---|---|
| Hugo runs | on Netlify | on your Mac |
| Cost | about 15 credits | nothing |
| Trigger | push a commit saying `[deploy]` | `scripts/deploy-manual.sh` |
| Who can do it | anyone with push access | whoever holds the token |
| Reads `netlify.toml` | yes | no |
| Deploy record | linked to the commit | shows as manual |

The plan allows 300 credits a month, roughly twenty builds, and they do not roll
over. That is the whole reason the manual route exists. Builds were already
blocked once, on 2026-09-20, with "account credit usage exceeded".

## Manual deploy

```bash
scripts/deploy-manual.sh --dry-run   # build and check, upload nothing
scripts/deploy-manual.sh             # build, check, upload, verify
```

It needs a Netlify personal access token, created at
<https://app.netlify.com/user/applications#personal-access-tokens>:

```bash
printf '%s' 'TOKEN' > ~/.netlify-token && chmod 600 ~/.netlify-token
```

The token controls the whole account, so treat it as a password.

The script refuses to run on a dirty working tree, so whatever goes live always
corresponds to a commit you can name later. Commit first, with `[skip build]`,
then deploy.

## The trap this script exists to prevent

**Netlify reads `netlify.toml` only when it runs the build itself.** A manual
deploy uploads the contents of `public/` and nothing else, so any redirect that
lives only in `netlify.toml` silently disappears. This happened on 2026-09-22:
`/weibel`, `/weibel/cv`, `/publications`, `/join`, `/deploy` and
`/course/cse218/enroll` all started returning 404 after a manual deploy.

The fix was to generate those rules into `public/_redirects` from
`layouts/index.redirects`, so they no longer depend on how the site is deployed.
They stay in `netlify.toml` too, where they still take precedence on a git
build, and the duplication is harmless.

**Adding a rewrite means adding it in `layouts/index.redirects`**, not only in
`netlify.toml`. The script checks three of them and stops if they are missing
from the built `_redirects`.

Old URLs for pages that still exist are different: those are `aliases:` in the
page's own front matter, and they already compile into `_redirects`. See the
README's "Old URLs" section.

## Keeping a local build honest

A local build differs from a Netlify one wherever configuration lives outside
the repo. The script checks what it can:

- **Hugo version.** Compared against `HUGO_VERSION` in `netlify.toml`. A
  different Hugo can render a different site, and the theme modules are pinned
  to this one.
- **Build flags.** `hugo --gc --minify --buildFuture -b https://hxi.ucsd.edu`
  with `HUGO_ENV=production`, copied from `netlify.toml`. Drop `--minify` and
  every page ships larger; drop `--buildFuture` and accepted-but-unpresented
  papers vanish.
- **Git info.** `netlify.toml` sets `HUGO_ENABLEGITINFO=true`, so the build
  needs real history. Building from a copy without `.git` changes page dates.
- **Base URL.** Wrong here and absolute links point at the wrong host.

What it cannot check: environment variables set in the Netlify UI, and build
plugins. `netlify-plugin-hugo-cache-resources` only caches between builds and
does not change output. **Adding a plugin that does change output would make
manual deploys diverge**, so re-read this file before adding one.

`DEPLOY_POLICY` and `scripts/netlify-ignore.sh` only govern git builds. A manual
deploy bypasses the gate entirely, by design.

## Which to use

Manual for routine batches, because credits are scarce and it is free.

A git `[deploy]` when you want the deploy tied to a commit in Netlify's history,
when you are not at the machine holding the token, or when someone else needs to
publish without it.
