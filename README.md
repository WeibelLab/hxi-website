# hxi.ucsd.edu

Source for the website of the **Human-centered eXtended Intelligence (HXI) Research Lab**
at UC San Diego, directed by [Nadir Weibel](https://hxi.ucsd.edu/author/nadir-weibel/).

[![Netlify Status](https://api.netlify.com/api/v1/badges/6d02b1d0-aca7-48d5-8696-8bd877f9817c/deploy-status)](https://app.netlify.com/sites/hxi-ucsd/deploys)

Built with [Hugo](https://gohugo.io) and the Wowchemy Research Group theme, hosted on
Netlify.

## How the site is put together

Everything a visitor sees comes from Markdown files under `content/`. There is no database
and no admin interface. A page is a folder, and the folder holds both the text and the
images that belong to it.

### The unit of content is a folder, not a file

Publications, people and projects each live in their own folder, with an `index.md`
(or `_index.md` for people) plus whatever assets belong to that item:

```
content/publication/2025-chidambaram-uist-drivesimquest/
    index.md          the metadata and abstract
    cite.bib          the BibTeX entry
    featured.jpg      optional image, picked up automatically by filename

content/authors/manas-bedmutha/
    _index.md         name, role, links, which group they appear under
    avatar.jpg        referenced as `avatar_filename: avatar`, without the extension
```

Hugo finds `featured.*` and `avatar.*` by name, so you never write an image path. The
folder name becomes the URL, which is why renaming one breaks every link pointing at it.

### What each section is

| Folder | Becomes | Holds |
|---|---|---|
| `content/publication/` | `/publication/` | 181 papers, one folder each |
| `content/project/` | `/research/` | 22 projects, one folder each |
| `content/authors/` | `/people/` and `/alumni/` | current members; `_alumni/` holds former ones |
| `content/course/` | `/teaching/` | courses |
| `content/faq/` | `/faq/` | joining the lab, contact, meeting us |
| `content/home/` | the front page | the front page's building blocks, see below |
| `content/research/`, `content/people/`, `content/alumni/` | those pages | not content, but the *assembly instructions* for them |
| `content/project-old/`, `content/archive/` | nothing | retired material, kept for reference |

### Pages are assembled from widgets

The front page, `/research`, and `/people` do not exist as documents. Each is built by
stacking widget files in order of a `weight` value, smallest first. The front page stacks
`content/home/welcome.md`, `slider.md`, `intro.md`, `cta.md`, `partners.md` and
`support.md`.

`/research` is two widgets over the same set of project folders:
`research.md` renders "Current Research Projects" and `foundations.md` renders "Earlier
Projects". A project moves between them by adding or removing the `Earlier` tag, not by
moving the folder. Both sections are filtered by the same two-axis Domain and Technology
control, defined in `research.md`.

`/people` and `/alumni` work the same way over `content/authors/`. Which heading a person
appears under is decided entirely by the `user_groups` value in their profile.

### How things find each other

Three fields do nearly all the cross-linking, and each one fails silently when wrong:

- **`authors:`** on a publication. A name that slugifies to a folder in `content/authors/`
  becomes a link to that person, shows the paper on their page, and renders their name in
  bold as a lab member. A name that does not match simply renders as plain text.
- **`projects:`** on a publication. Names a project folder. The paper then appears in that
  project's publication list, and the project appears on the paper's page. The project page
  needs no edit; the list is generated.
- **`categories:`** on a publication. Mirrors `projects:` and exists only to drive the
  "Related" suggestions, because Hugo cannot index the `projects` field directly. It is
  hidden from view by CSS.

Tags and publication types are also taxonomies, so `/tag/CHI/` and similar pages exist
automatically.

### Everything else

| Path | What it controls |
|---|---|
| `config/_default/config.yaml` | site-wide Hugo settings, taxonomies, related-content weights |
| `config/_default/params.yaml` | theme options, colours, fonts, plugins |
| `config/_default/menus.yaml` | the navigation bar |
| `layouts/` | the four templates that override the theme, listed near the end of this file |
| `assets/` | custom SCSS and the JavaScript for the research-page filters |
| `static/images/` | logos used in the funding rows on project pages |
| `netlify.toml` | build command, redirects, and the deploy gate |

The theme itself is not in this repository. It is pulled in as a Hugo module, pinned in
`go.mod`, so there is nothing to edit there and upgrading it is deliberately not routine.

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
