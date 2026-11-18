# Public Learning Site Rules

## Goal
Publish clear, accurate, accessible, and maintainable educational material.

## Privacy boundary
The private knowledge repository provides proposed insights, not a direct publishing feed.
Never copy private notes, chat transcripts, or attachments wholesale into this public repository.

## Editorial rules
1. Read an existing lesson in full before editing.
2. Preserve interactive diagrams, mathematics, worked examples and teaching continuity.
3. Prefer focused changes; justify and review substantial rewrites.
4. Check internal links, page navigation, mobile layout, accessibility and deployment routes.
5. Preserve provenance and verify technical claims.
6. Prefer reviewable pull requests to direct publishing.
7. Do not delete working learning material without explicit approval.

## Site layout and deployment
- **Canonical site pages live at repository root** on `main`.
- Pages is currently built from the repository root according to deployment logs.
- Pages Settings -> Deploy from a branch -> main -> /(root).
- Keep `.nojekyll` at the repository root.
- `docs/` contains temporary migration snapshots; do not update it instead of the root site.
- Execute `python3 scripts/check_static_links.py .` before publishing.
- If switching to Astro + Starlight, update the publishing workflow and validation together.
