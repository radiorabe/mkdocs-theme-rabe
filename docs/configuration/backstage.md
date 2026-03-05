# Backstage / TechDocs Integration

[Backstage](https://backstage.io) can render repository documentation via
its **TechDocs** plugin.  The RaBe Backstage instance uses a custom
publisher that reads pre-built documentation directly from **GitHub Pages**,
so you do **not** need a separate TechDocs build step.

## What your repo needs to do

1. Build and deploy your docs to GitHub Pages using the standard
   [MkDocs release workflow](#ci-cd).
2. Ensure `techdocs_metadata.json` is present at the root of the published
   site.  The easiest way is to build via `techdocs-cli generate` instead
   of plain `mkdocs build`:

   ```bash
   pip install mkdocs-theme-rabe "@techdocs/cli"
   npx @techdocs/cli generate --no-docker
   ```

3. Set the `metadata.name` in your `catalog-info.yaml` to the **lowercase
   repository name** – the Backstage publisher maps entity names directly
   to GitHub Pages path segments.

## CI/CD

Use the reusable MkDocs workflow from `radiorabe/actions`:

```yaml title=".github/workflows/release.yaml"
name: Release

on:
  push:
    branches: [main]
  pull_request:

permissions: {}

jobs:
  release-mkdocs:
    permissions:
      contents: write
    uses: radiorabe/actions/.github/workflows/release-mkdocs.yaml@v0
```

For Python packages that also publish to PyPI, use the Poetry release workflow
instead (it calls `mkdocs gh-deploy` automatically):

```yaml title=".github/workflows/release.yaml"
name: Release

on:
  release:
    types: [published]
  push:
    branches: [main]
  pull_request:

permissions: {}

jobs:
  release:
    permissions:
      contents: write
    secrets:
      RABE_PYPI_TOKEN: ${{ secrets.RABE_PYPI_TOKEN }}
    uses: radiorabe/actions/.github/workflows/release-python-poetry.yaml@v0
```

## Shadow DOM compatibility

Backstage injects TechDocs HTML into a
[shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM).
The RaBe theme avoids global `document`-level selectors that would break
inside a shadow root, keeping all styles scoped to CSS custom properties
that Material already exposes.

!!! warning "JavaScript features"
    Some MkDocs-Material features (e.g. the search overlay, clipboard
    copy) rely on global JS that may not function inside the Backstage
    shadow DOM.  They degrade gracefully – the content remains readable.
