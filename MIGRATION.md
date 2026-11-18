# GitHub Pages Migration Record

## Source
Repository: `tjz12345/image-prompt-reverse`
Branch: `gh-pages`
Source files are retained and not modified.

## Target
Repository: `tjz12345/learning-hub`
Branch: `main`
Publish directory: `docs/`

| Original path | New path |
| --- | --- |
| `index.html` | `docs/cryptography/index.html` |
| `buck-5v/index.html` | `docs/buck-5v/index.html` |
| `learning-lab/index.html` | `docs/learning-lab/index.html` |
| `learning-lab/electricity-foundations/index.html` | `docs/learning-lab/electricity-foundations/index.html` |

The new `docs/index.html` is a curated learning-portal entry page. The one original
cross-link pointing to the old Buck URL in the electronics lesson was updated to
a relative link inside the new public repository.

## Activation required
An administrator must open **Settings -> Pages** in the destination repository,
choose **Deploy from a branch**, branch **main**, folder **/docs**, then save.

Expected default URL after publishing:
https://tjz12345.github.io/learning-hub/

Do not disable the old Pages site until the new routes have been smoke-tested.
Custom domain setup is intentionally deferred to avoid breaking working URLs.
