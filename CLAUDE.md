# HXI Lab website (hxi.ucsd.edu)

Hugo 0.89.2 extended + Wowchemy "Research Group" theme, modules pinned in `go.mod`.
Deployed on Netlify as site `hxi-ucsd`. Repository: `WeibelLab/hxi-website`.

## Working in this checkout

The working tree lives on Google Drive, so git is very slow here. Run every git
command in the background. Build and preview in a scratchpad clone instead of in
place: rsync `content`, `config`, `assets`, `layouts` and `static` into the clone
and run `hugo` there. A scratchpad clone has no `.git`, so Hugo logs one error
about reading the git log; the build itself still completes.

## Redirects

`layouts/index.redirects` compiles `public/_redirects` from each page's `aliases:`
front matter. It also repeats the rewrites from `netlify.toml`, because
`netlify.toml` is read only when Netlify runs the build and is invisible to a
manual deploy. Adding an alias to a page is enough; nothing else needs editing.

## Publishing without build credits

`scripts/deploy-manual.sh` builds locally and uploads through the Netlify API.
A manual deploy consumes zero build minutes (`manual_deploy: true`,
`build_id: null`). The API token is at `~/.netlify-token`, mode 600. The script
refuses to run if the Hugo version does not match `HUGO_VERSION`, if the tree is
dirty, if `.git` is missing, if the base URL is wrong, or if the netlify.toml
rewrites are absent from the generated `_redirects`.

Plan credits (Open Source, 10,000/month) are consumed by bandwidth and web
requests, not by builds. The real remaining figure appears only in the billing
UI; the API's plan metadata is static and does not report usage.

## Publication PDFs

Full texts are not in this repository. They live in the private
`WeibelLab/hxi-papers` repo, one directory per publication slug, holding the PDF
plus `cite.bib` and the chosen `featured.jpg`. `papers/` is in `.gitignore`, and
the archive is deliberately not a submodule, so a normal checkout of this site
does not pull roughly a gigabyte of PDFs.

PDF file naming: `Year_FirstAuthorLastName_Venue_ShortTitle.pdf`.

Publishers block scripted downloads through bot detection rather than paywalls,
so a VPN does not help and headless Chrome does not either. ACM and IEEE need a
logged-in browser session. PMC uses a proof-of-work cookie that a real browser
clears on its own. eScholarship serves PDFs to curl when the request carries a
browser User-Agent plus `Referer` and `Sec-Fetch-*` headers.

## Publication figures

Each publication's `featured.jpg` is a figure taken from the paper itself.
Figures are located by their `Figure N` caption, then the crop is reduced to the
artwork's own bounding box so captions, running heads, page numbers and author
blocks fall outside it, and rendered at 300 dpi. Short text touching the artwork
(axis labels, legends, panel letters) is kept; prose and caption lines are not.

A small number of publications keep an earlier crop because the tighter framing
pulled in a neighbouring figure or an adjacent text column.

## Front matter

`projects:` and `slides:` belong at the top level, not nested inside the `image:`
block. Five publications had them nested, which silently removed those papers
from their project pages.

## Conventions

Contact order is Design Lab (DIB) first, then the CSE building. The footer's blue
bar uses `#0d1f45`, matching the navbar. The Netlify build badge appears on the
home page only.
