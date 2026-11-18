# Learning Hub

Public technical learning site and interactive engineering laboratory.

## Links
- Website (when Pages deployment is live): https://tjz12345.github.io/learning-hub/
- Repository: https://github.com/tjz12345/learning-hub
- Private source of proposed notes: `tjz12345/personal-knowledge_hub` (private, not published).

## Current site source
The site is served from the **repository root** on `main`, not from `docs/`.
The initial Pages deployment returned 404 because it published the root while HTML files existed only under `docs/`. This was corrected by placing the complete site at the root.

Canonical pages:
- `index.html` -> `/`: learning portal
- `cryptography/index.html` -> `/cryptography/`
- `learning-lab/index.html` -> `/learning-lab/`
- `learning-lab/electricity-foundations/index.html` -> `/learning-lab/electricity-foundations/`
- `buck-5v/index.html` -> `/buck-5v/`

The `docs/` directory is a temporary migration snapshot. **Edit root pages** for future updates; do not edit `docs/` as the primary source. Remove snapshots only after site verification.

## Pages settings
Under Settings -> Pages:
- Source: **Deploy from a branch**
- Branch: `main`
- Folder: `/(root)`

## Validation
The GitHub Actions workflow validates root landing-page existence and local page links.
The original pages in `tjz12345/image-prompt-reverse` remain untouched.
