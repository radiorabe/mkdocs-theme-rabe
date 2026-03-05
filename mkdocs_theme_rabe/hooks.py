"""MkDocs hooks for the RaBe theme.

These hooks are automatically called by MkDocs at various stages of the
build process. Register them in `mkdocs.yml`:

```yaml
hooks:
  - mkdocs_theme_rabe/hooks.py
```

When the package is installed, import the hook directly:

```python
from mkdocs_theme_rabe.hooks import on_page_context
```
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.nav import Navigation
    from mkdocs.structure.pages import Page


def on_page_context(
    context: dict,
    *,
    page: "Page",
    config: "MkDocsConfig",
    nav: "Navigation",
) -> dict:
    """Inject extra template context variables for every page.

    Adds ``rabe_theme`` dict with handy metadata that templates can
    reference.
    """
    context["rabe_theme"] = {
        "version": _get_version(),
        "is_home": page.is_homepage,
    }
    return context


def _get_version() -> str:
    """Return the installed package version."""
    try:
        from importlib.metadata import PackageNotFoundError, version

        return version("mkdocs-theme-rabe")
    except PackageNotFoundError:  # pragma: no cover
        return "dev"
