# Theme Options

`mkdocs-theme-rabe` extends
[MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) and
accepts **all** of its theme options.  This page documents the RaBe
defaults and any theme-specific additions.

## Palette

The canonical RaBe palette uses `#00c9bf` (teal) as both primary and accent
colour, with the **slate** (dark) scheme as the default presentation mode.

```yaml title="mkdocs.yml"
theme:
  name: rabe
  palette:
    - scheme: slate       # dark mode
      primary: "#00c9bf"
      accent: "#00c9bf"
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
    - scheme: default     # light mode
      primary: "#00c9bf"
      accent: "#00c9bf"
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
```

## Typography

```yaml title="mkdocs.yml"
theme:
  font:
    text: Roboto
    code: Roboto Mono
```

## Logo & Icons

```yaml title="mkdocs.yml"
theme:
  icon:
    repo: fontawesome/brands/github
    logo: material/radio   # the RaBe radio antenna icon
```

## Recommended Features

The following feature flags are enabled on the reference site and are
recommended for all RaBe repos:

```yaml title="mkdocs.yml"
theme:
  features:
    - content.code.annotate
    - content.code.copy
    - navigation.footer
    - navigation.indexes
    - navigation.sections
    - navigation.tabs
    - navigation.top
    - navigation.tracking
    - search.highlight
    - search.share
    - search.suggest
    - toc.follow
```

## Extra Social Links

```yaml title="mkdocs.yml"
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/radiorabe/my-project
      name: GitHub
  generator: false   # hides "Made with Material for MkDocs"
```
