# LLM task brief: migrate this project to Great Docs
Your objective is to upgrade this repository to use Great Docs for local docs authoring, link validation, and GitHub Pages deployment.

Use these instructions as the source of truth and execute them end-to-end unless blocked.

## Non-negotiables
- Use `uv` for Python dependency and tooling management.
- Keep commands and workflow updates portable across macOS, Linux, and Windows where possible.
- Prefer additive, low-risk changes; avoid unrelated refactors.
- Validate locally before proposing release/deploy changes.

## Implementation plan
1. Audit current docs/tooling setup
   - Inspect existing docs files, CI workflows, `README.md`, `justfile`, and dependency configuration.
   - Identify any current docs build/deploy path so Great Docs can replace or integrate cleanly.

2. Add Great Docs dependency and configuration
   - Add `great-docs` as a dev dependency via `uv`.
   - Initialise Great Docs configuration (`great-docs.yml`) if missing.
   - Set key config values explicitly:
     - `site_url` to the final GitHub Pages URL.
     - source branch/path to the default branch and source tree used by this repo.

3. Add/refresh GitHub Actions docs workflow
   - Create or update `.github/workflows/docs.yml` using Great Docs conventions.
   - Ensure dependency install uses:
     - `uv sync --frozen --dev`
   - Ensure workflow includes build and GitHub Pages publish jobs.
   - Confirm action versions are current and consistent with repo standards.

4. Add local docs recipes (if `justfile` exists)
   - Add self-documenting recipes:
     - docs init
     - docs build
     - docs preview
     - docs scan
     - docs setup pages
     - docs link check (prepublish profile)
     - docs link check strict
     - docs workflow shortcuts

5. Implement practical link-check strategy
   - Add a prepublish check command that can ignore known not-yet-live URLs (for initial rollout only).
   - Keep a strict check variant with no ignores.
   - Document why prepublish ignores exist and when to remove them.

6. Update project docs
   - Update `README.md` with Great Docs local usage commands.
   - Add or update a docs setup guide (for example in `docs/`).
   - Ensure contributor-facing docs include expected local QA flow.

7. Validate locally
   - Run docs build.
   - Run prepublish docs link checks.
   - Run strict link checks where feasible.
   - Run project QA/lint/tests to ensure no regressions.

8. Verify GitHub Pages settings assumptions
   - Confirm deployment expects GitHub Pages **workflow** mode rather than legacy branch mode.
   - Ensure docs workflow file is present on the default branch path expected by GitHub.
   - Note: if workflow exists only on a feature branch, Pages will remain 404 until merged.

9. Prepare concise rollout notes
   - Summarise what changed, validation evidence, and any temporary caveats.
   - Include a short cleanup follow-up list (for example removing temporary link-check ignores after first live publish).

## Known pitfalls from prior rollout
- GitHub Pages can stay on legacy mode and serve 404 even when docs workflow exists.
- If `docs.yml` is not on the default branch, no docs workflow runs for production deploy.
- Local preview may show non-critical 404s (`favicon`, apple-touch-icon) and transient broken pipe/reset messages.
- YAML author metadata can break parsing if values with special characters are not formatted safely.

## Completion criteria
- Great Docs is installed and configured.
- Docs workflow exists and is valid.
- Local docs build + link checks pass (with documented prepublish vs strict behaviour).
- GitHub Pages path and workflow assumptions are documented and correct.
- Repo docs clearly explain how to build, preview, and validate docs.
