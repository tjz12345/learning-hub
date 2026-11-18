# Learning Hub

Public technical learning site and interactive engineering laboratory.

## Links
- Source repository: https://github.com/tjz12345/learning-hub
- Planned GitHub Pages URL: https://tjz12345.github.io/learning-hub/
- Private knowledge source: a separate, non-public repository. Never copy raw private notes here.

## Site layout
Static HTML is currently published from `docs/` on `main`:
- `docs/index.html`: new learning portal
- `docs/cryptography/index.html`: cryptography interactive textbook
- `docs/learning-lab/index.html`: engineering laboratory
- `docs/learning-lab/electricity-foundations/index.html`: electronics foundations
- `docs/buck-5v/index.html`: Buck converter interactive lesson

## Publish
1. Visit Settings -> Pages.
2. Select **Deploy from a branch**.
3. Choose branch **main** and folder **/docs**.
4. Save. Verify the live Pages URL.
5. After review, merge only vetted website changes into `main`.

Existing content was copied from the `gh-pages` branch of
`tjz12345/image-prompt-reverse` without deleting or modifying the source.

A future Astro + Starlight build may replace static `docs/` publishing
once the initial migration is verified.
