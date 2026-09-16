# hxi.ucsd.edu

Source for the website of the **Human-centered eXtended Intelligence (HXI) Research Lab**
at UC San Diego, directed by [Nadir Weibel](https://hxi.ucsd.edu/author/nadir-weibel/).

[![Netlify Status](https://api.netlify.com/api/v1/badges/6d02b1d0-aca7-48d5-8696-8bd877f9817c/deploy-status)](https://app.netlify.com/sites/hxi-ucsd/deploys)

The site is [Hugo](https://gohugo.io) with the Wowchemy Research Group theme, hosted on
Netlify. Everything a visitor sees comes from Markdown files under `content/`. There is no
database and no admin interface, so editing the site means editing text files in this
repository.

## The site, page by page

| | |
|---|---|
| **[Home](https://hxi.ucsd.edu/)**<br><br>What the lab is, a photo slider, the calls to action, partners and funders.<br><br>A stack of widget files in `content/home/`, ordered by `weight`: `welcome.md`, `slider.md`, `intro.md`, `cta.md`, `partners.md`, `support.md`. | <img src="docs/screenshots/home.png" width="300"> |
| **[Research](https://hxi.ucsd.edu/research/)**<br><br>Every project, split into current and earlier work, with Domain and Technology filters.<br><br>Two portfolio widgets over `content/project/`: `content/research/research.md` and `foundations.md`. A project moves between the sections by gaining or losing the `Earlier` tag. | <img src="docs/screenshots/research.png" width="300"> |
| **[People](https://hxi.ucsd.edu/people/)**<br><br>Current members, grouped by role.<br><br>`content/people/people.md` over the profile folders in `content/authors/`. The grouping comes from each person's own `user_groups`. | <img src="docs/screenshots/people.png" width="300"> |
| **[Alumni](https://hxi.ucsd.edu/alumni/)**<br><br>Former members, same layout and different groups.<br><br>`content/alumni/alumni.md`. Their profile folders sit in `content/authors/_alumni/`. | <img src="docs/screenshots/alumni.png" width="300"> |
| **[Publications](https://hxi.ucsd.edu/publication/)**<br><br>The full list, newest first, with search and filters.<br><br>One folder per paper in `content/publication/`. `layouts/section/publication.html` sorts preprints after peer-reviewed papers within a year. | <img src="docs/screenshots/publications.png" width="300"> |
| **[Teaching](https://hxi.ucsd.edu/teaching/)**<br><br>The courses the lab teaches.<br><br>One folder per course in `content/course/`. | <img src="docs/screenshots/teaching.png" width="300"> |
| **[FAQ](https://hxi.ucsd.edu/faq/)**<br><br>Joining the lab, getting in touch, letters and committee requests.<br><br>One folder per question in `content/faq/`. | <img src="docs/screenshots/faq.png" width="300"> |

And the three page types that make up most of the site:

| | |
|---|---|
| **[A project](https://hxi.ucsd.edu/project/simulated-patients/)**<br><br>Description, images, funders, and a publication list that is generated rather than written: it is every paper whose `projects:` field names this folder.<br><br>`content/project/<slug>/index.md` plus its images. | <img src="docs/screenshots/project-page.png" width="300"> |
| **[A publication](https://hxi.ucsd.edu/publication/2025-chidambaram-uist-drivesimquest/)**<br><br>Authors, abstract, venue, and the Cite and DOI buttons. Author names matching a profile become links and render in bold.<br><br>`content/publication/<slug>/index.md` plus `cite.bib`. | <img src="docs/screenshots/publication-page.png" width="300"> |
| **[A person](https://hxi.ucsd.edu/author/nadir-weibel/)**<br><br>Bio, links, and every paper naming them, collected automatically.<br><br>`content/authors/<name>/_index.md` plus `avatar.jpg`. | <img src="docs/screenshots/author-page.png" width="300"> |

## How the site is put together

**A page is a folder, not a file.** Publications, people and projects each get their own
folder holding the text and its images:

```
content/publication/2025-chidambaram-uist-drivesimquest/
    index.md          metadata and abstract
    cite.bib          the BibTeX entry
    featured.jpg      optional, found by filename
```

Hugo picks up `featured.*` and `avatar.*` by name, so you never write an image path. The
folder name becomes the URL, which is why renaming one breaks every link to it.

**Section pages are assembled, not written.** The home page, `/research` and `/people` do
not exist as documents. Each stacks widget files in order of a `weight` value, as listed in
the table above.

**Three fields do the cross-linking**, and each fails silently when wrong:

- `authors:` on a publication. A name that slugifies to a folder in `content/authors/`
  links to that person, puts the paper on their page, and bolds them as a lab member.
- `projects:` on a publication. Names a project folder, which then lists the paper
  automatically. The project page itself needs no edit.
- `categories:` mirrors `projects:` and exists only to drive the "Related" suggestions,
  because Hugo cannot index the `projects` field directly. It is hidden from view.

**Everything else:** `config/_default/` holds the Hugo settings, theme options and
navigation; `assets/` the custom SCSS and the research-page filter JavaScript;
`static/images/` the funder logos; `netlify.toml` the build, redirects and deploy gate.
The theme itself is a Hugo module pinned in `go.mod` and is not in this repository.

## I just want to add a paper or update my profile

You do not need to install anything, and you do not need to know Hugo or Markdown.
Ask Claude or ChatGPT to do it, using the lab's packaged helper. Nadir has the files and
the setup instructions; ask him for `hxi-website.zip` (Claude) or
`hxi-website-chatgpt.zip` (ChatGPT, which also works for Gemini and Copilot).

You will need **write access to this repository**. Send Nadir your GitHub username.

If you would rather do it by hand, copy the shape of an existing neighbour rather than
writing a file from scratch. The paths are in the tables above.

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

- **`user_groups` must match one of the strings the people widget lists.** `Ph.D` has one period and
  `Master` is singular. A value not on that list removes the person from `/people` with no
  error. Copy it from an existing profile rather than retyping it.
- **`projects:` values are project folder names.** A slug that does not exist just does
  nothing.
- **Spell out every author**, in paper order, never "et al.". A misspelled name silently
  costs that person the credit.
- **Nothing under review goes on the site** unless it is already on arXiv.
- Future dates are fine. The site builds with `buildFuture`, so an accepted paper can
  carry its real conference date.

## Bibliography

The full publication list is exported as BibTeX at
[hxi.ucsd.edu/hxi.bib](https://hxi.ucsd.edu/hxi.bib), generated at build time from each
publication's own `cite.bib`. There is no hand-maintained master `.bib` file, deliberately:
the previous one silently went stale for four years.

## Building locally

Requires Hugo **extended** 0.89.2, the version Netlify uses. Newer versions break this
theme's pinned modules.

```bash
hugo server
```

Then open http://localhost:1313. Restart the server after changing anything in `config/`,
`static/`, `assets/js/` or `layouts/`, and after renaming a folder. Live reload does not
pick those up reliably and will quietly serve stale content.

## Layout overrides

Everything in `layouts/` overrides the theme. Keep this list short.

| File | Why |
|---|---|
| `layouts/section/publication.html` | Sorts preprints last within each year |
| `layouts/authors/list.html` | Groups people by `user_groups` on `/people` and `/alumni` |
| `layouts/partials/widgets/portfolio.html` | Adds `exclude_tags` and two-axis filtering on `/research` |
| `layouts/publication/list.bib` | Generates the combined BibTeX export |

Screenshots in `docs/screenshots/` are used only by this README.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report concerns to hxi@ucsd.edu.
