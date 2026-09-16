# hxi.ucsd.edu

Source for the website of the **Human-centered eXtended Intelligence (HXI) Research Lab**
at UC San Diego, directed by [Nadir Weibel](https://hxi.ucsd.edu/author/nadir-weibel/).

[![Netlify Status](https://api.netlify.com/api/v1/badges/6d02b1d0-aca7-48d5-8696-8bd877f9817c/deploy-status)](https://app.netlify.com/sites/hxi-ucsd/deploys)

Built with [Hugo](https://gohugo.io) and the Wowchemy Research Group theme, hosted on
Netlify.

## I just want to add a paper or update my profile

You do not need to install anything, and you do not need to know Hugo or Markdown.
Ask Claude or ChatGPT to do it, using the lab's packaged helper. Nadir has the files and
the setup instructions; ask him for `hxi-website.zip` (Claude) or
`hxi-website-chatgpt.zip` (ChatGPT, and works for Gemini and Copilot too).

You will need **write access to this repository**. Send Nadir your GitHub username.

If you would rather do it by hand, the two things you are most likely to touch are:

| What | Where |
|---|---|
| A publication | `content/publication/<year>-<lastname>-<venue>-<short>/` — `index.md` plus `cite.bib` |
| A person | `content/authors/<firstname-lastname>/_index.md`, plus `avatar.jpg` in the same folder |
| A project | `content/project/<slug>/index.md` |

Copy the shape of an existing neighbour rather than writing one from scratch.

## Committing does not publish

The live site is published in batches, not on every commit. Netlify's free tier gives 300
build credits a month and a full rebuild costs about 15, so roughly 20 publishes a month
for the whole lab.

`scripts/netlify-ignore.sh` enforces this. It reads the `DEPLOY_POLICY` environment
variable set in the Netlify UI:

| `DEPLOY_POLICY` | Behaviour |
|---|---|
| unset or `manual` | Nothing publishes unless the commit message contains `[deploy]` |
| `auto` | Everything publishes except commits containing `[skip build]` |

Commit as often as you like; it costs nothing. Your change goes live at the next publish.
**Do not put `[deploy]` in a commit message** unless you are the one releasing the queue,
because it publishes everything anyone else has queued too.

## Conventions that matter

These are the ones that fail *silently*, producing a clean build with your content missing:

- **`user_groups` must match one of eight exact strings.** `Ph.D` has one period and
  `Master` is singular. A value not on the list removes the person from `/people` with no
  error. See any existing profile for the list.
- **`projects:` values are project folder names.** A slug that does not exist just does
  nothing. It also drives the "Related" publications, via `categories:`.
- **Spell out every author**, in paper order, never "et al.". A name that exactly matches
  a folder in `content/authors/` becomes a link to that person and makes the paper appear
  on their page; a misspelling silently costs them the credit.
- **Nothing under review goes on the site** unless it is already on arXiv.
- Future dates are fine. The site builds with `buildFuture`, so an accepted paper can
  carry its real conference date.

## Bibliography

The lab's full publication list is exported as BibTeX at
[hxi.ucsd.edu/hxi.bib](https://hxi.ucsd.edu/hxi.bib), generated at build time from each
publication's own `cite.bib`. There is no hand-maintained master `.bib` file, deliberately:
the previous one silently went stale for four years.

## Building locally

Requires Hugo **extended** 0.89.2 (the version Netlify uses; newer versions break this
theme's pinned modules).

```bash
hugo server
```

Then open http://localhost:1313. Restart the server after changing anything in `config/`,
`static/`, `assets/js/`, or `layouts/`, and after renaming a folder — live reload does not
pick those up reliably and will quietly serve stale content.

## Layout overrides

Everything in `layouts/` overrides the theme. Keep this list short.

| File | Why |
|---|---|
| `layouts/section/publication.html` | Sorts preprints last within each year |
| `layouts/authors/list.html` | Groups people by `user_groups` on `/people` and `/alumni` |
| `layouts/partials/widgets/portfolio.html` | Adds `exclude_tags` and two-axis filtering on `/research` |
| `layouts/publication/list.bib` | Generates the combined BibTeX export |

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report concerns to hxi@ucsd.edu.
