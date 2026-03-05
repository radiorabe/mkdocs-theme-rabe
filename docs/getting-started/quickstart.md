# Quick Start

After [installing](installation.md) the package, create a minimal
`mkdocs.yml` at the root of your repository:

```yaml title="mkdocs.yml"
site_name: My Project
repo_url: https://github.com/radiorabe/my-project

theme:
  name: rabe
  font:
    text: Roboto
    code: Roboto Mono
  icon:
    repo: fontawesome/brands/github
    logo: material/radio
  features:
    - content.code.copy
    - navigation.footer
    - navigation.top
    - search.highlight
    - search.suggest

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - toc:
      permalink: true
```

Then add a `docs/index.md` and run:

```bash
mkdocs serve   # local preview
mkdocs build   # produce the ./site directory
```

## Using the home-page template

To get the full RaBe hero banner on your landing page, add front-matter
to `docs/index.md`:

```markdown
---
template: home.html
hero_cta_primary:
  text: Get Started
  url: getting-started/
hero_cta_secondary:
  text: View on GitHub
  url: https://github.com/radiorabe/my-project
---

# My Project

Short description shown below the hero.
```

## Adding llms.txt

To generate a machine-readable `/llms.txt` file with your documentation
(useful for AI tools and LLM indexing), add the `llmstxt` plugin:

```yaml title="mkdocs.yml"
plugins:
  - search
  - llmstxt:
      markdown_description: |
        Brief description of your project for LLM context.
      sections:
        Docs:
          - "**/*.md"
```

The `mkdocs-llmstxt` package is bundled as a dependency of `mkdocs-theme-rabe`
so no separate install is required.

## Adding the hooks

Optionally register the built-in hooks to get extra template variables:

```yaml title="mkdocs.yml"
hooks:
  - mkdocs_theme_rabe/hooks.py
```

!!! note
    When the package is installed as an editable source checkout, provide
    the absolute import path instead:
    `hooks: [path/to/mkdocs_theme_rabe/hooks.py]`
