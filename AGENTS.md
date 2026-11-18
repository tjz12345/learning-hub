# Public Learning Site Rules

## Goal
Publish clear, accurate, accessible, and maintainable educational material.

## Source boundary
The private knowledge repository is a source of proposed learning insights, not a direct publication feed.
Never copy private notes, chat transcripts, or attachments wholesale.

## Update protocol
1. Read the existing lesson before editing it.
2. Preserve working interactions, diagrams, mathematical notation, and explanatory continuity.
3. Make minimal, focused edits and keep evidence for technical corrections.
4. Validate internal links, navigation, mobile layout, accessibility and publication routes.
5. Record source and destination for migrations.
6. Propose reviewed changes through a pull request whenever possible.
7. Do not silently delete prior lessons or overwrite substantial content.

## Current deployment
- Current site source: `docs/` on the `main` branch.
- Pages configuration: Settings -> Pages -> Deploy from a branch -> main -> /docs.
- Preserve `docs/.nojekyll` for raw HTML publication.
- A later migration to Astro + Starlight may change the build source after validation.
