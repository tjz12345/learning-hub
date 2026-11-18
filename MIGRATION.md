# GitHub Pages Migration Record

## Legacy source
- Repository: `tjz12345/image-prompt-reverse`
- Branch: `gh-pages`
- Original files remain unchanged.

## New destination
- Repository: `tjz12345/learning-hub`
- Branch: `main`
- **Published site directory: repository root (`/`)**

| Old path | Published path |
| --- | --- |
| `index.html` | `cryptography/index.html` |
| `buck-5v/index.html` | `buck-5v/index.html` |
| `learning-lab/index.html` | `learning-lab/index.html` |
| `learning-lab/electricity-foundations/index.html` | `learning-lab/electricity-foundations/index.html` |

A new homepage was added as `index.html`.
The single legacy hardcoded Buck link inside the electronics lesson was rewritten to the new relative URL.

## First-deployment 404 and correction
The initial import placed files exclusively in `docs/`, but the GitHub Pages build was processing the **repository root**.
The deployment succeeded technically, yet `/learning-hub/` had no root `index.html` and produced a 404.

Fix commit `8b70ceb30e71adf63a5c55e816c7cddb75f9190d` placed the website files at the actual publishing root, preserving the original content and legacy `docs/` snapshots.

The canonical authoring location is now the root. Do not maintain two divergent copies.
Verify the live site and the four migrated routes before removing old backups.

## Pages configuration
Under Settings -> Pages choose:
- Deploy from a branch
- Branch: `main`
- Folder: `/(root)`

Default site URL: https://tjz12345.github.io/learning-hub/

Custom domain setup is deferred. Do not remove the old Pages site before live validation.
