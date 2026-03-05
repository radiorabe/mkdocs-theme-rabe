# Hooks API

The `mkdocs_theme_rabe.hooks` module provides MkDocs
[hooks](https://www.mkdocs.org/user-guide/configuration/#hooks) that add
extra template context variables and other conveniences.

## Registration

```yaml title="mkdocs.yml"
hooks:
  - mkdocs_theme_rabe/hooks.py
```

## API

::: mkdocs_theme_rabe.hooks
    options:
      show_root_heading: true
      heading_level: 3
