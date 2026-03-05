# Agent Instructions: radiorabe/mkdocs-theme-rabe

## Repository Purpose

This repository contains the **mkdocs-theme-rabe** Python package — a centralised
MkDocs theme for Radio Bern RaBe projects. It bundles the RaBe brand identity
(`#00c9bf` teal), required MkDocs dependencies, and custom rendering logic so every
`radiorabe` repository's documentation looks and feels consistent.

The full documentation is published at
[radiorabe.github.io/mkdocs-theme-rabe](https://radiorabe.github.io/mkdocs-theme-rabe/).

## Repository Structure

```
mkdocs_theme_rabe/
  theme/             # MkDocs theme (registered as name: rabe via entry point)
    assets/          # CSS and other static assets
    mkdocs_theme.yml # Theme defaults (palette, locale, extends: material)
    main.html        # Base template override (injects rabe.css)
    home.html        # Home-page hero template
  hooks.py           # MkDocs hook: injects rabe_theme context into every page
docs/                # Self-documenting MkDocs site
tests/
  test_hooks.py      # Unit tests for hooks.py
  playwright/        # Visual regression snapshot tests
pyproject.toml       # Package metadata and dependencies
mkdocs.yml           # MkDocs config for this repo's own docs site
```

## Conventions

- **Brand colour**: `#00c9bf` (teal) — used as `--md-primary-fg-color` and
  `--md-accent-fg-color` in both the `default` (light) and `slate` (dark) schemes.
- **License**: AGPL-3.0-or-later (matches all other `radiorabe` repos).
- **Python style**: Google-style docstrings; markdown fenced code blocks inside
  docstrings (not RST `.. code-block::` directives).
- **Versioning**: Semantic releasing via `go-semantic-release` driven by
  [conventional commits](https://www.conventionalcommits.org) — no manual
  version bumps in source code.

## Linting and Testing

```bash
# Unit tests (fast, no browser required)
poetry run pytest tests/test_hooks.py

# Visual snapshot tests (requires Chromium)
poetry run playwright install chromium --with-deps
poetry run mkdocs build --strict
poetry run pytest tests/playwright/ -v

# Rebuild baseline snapshots after intentional visual changes
poetry run pytest tests/playwright/ --snapshot-update

# Build the documentation site
poetry run mkdocs build --strict
```

## llms.txt

- [radiorabe.github.io/mkdocs-theme-rabe/llms.txt](https://radiorabe.github.io/mkdocs-theme-rabe/llms.txt) – this repo (auto-generated at build time)
- [radiorabe.github.io/actions/llms.txt](https://radiorabe.github.io/actions/llms.txt) – reusable GitHub Actions workflows for radiorabe CI/CD
- [docs.github.com/llms.txt](https://docs.github.com/llms.txt) – GitHub Actions and GitHub Pages
