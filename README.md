# mkdocs-theme-rabe

[![PyPI](https://img.shields.io/pypi/v/mkdocs-theme-rabe)](https://pypi.org/project/mkdocs-theme-rabe/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](LICENSE)

Centralised MkDocs theme for [Radio Bern RaBe](https://rabe.ch) GitHub
repositories. Bundles the RaBe brand identity (`#00c9bf` teal), required
dependencies, and custom rendering logic so every project automatically
looks and feels consistent.

## Quick start

```bash
pip install mkdocs-theme-rabe
```

```yaml title="mkdocs.yml"
site_name: My Project
repo_url: https://github.com/radiorabe/my-project

theme:
  name: rabe
  palette:
    - scheme: slate
      primary: "#00c9bf"
      accent: "#00c9bf"
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
    - scheme: default
      primary: "#00c9bf"
      accent: "#00c9bf"
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
  font:
    text: Roboto
    code: Roboto Mono
  icon:
    repo: fontawesome/brands/github
    logo: material/radio
```

Full documentation: <https://radiorabe.github.io/mkdocs-theme-rabe/>

## Bundled dependencies

Installing `mkdocs-theme-rabe` also installs:

- [MkDocs](https://www.mkdocs.org)
- [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/)
- [mkdocstrings\[python\]](https://mkdocstrings.github.io)
- [pymdown-extensions](https://facelessuser.github.io/pymdown-extensions/)
- [mkdocs-section-index](https://oprypin.github.io/mkdocs-section-index/)
- [mkdocs-gen-files](https://oprypin.github.io/mkdocs-gen-files/)
- [mkdocs-literate-nav](https://oprypin.github.io/mkdocs-literate-nav/)

## License

[AGPL-3.0-or-later](LICENSE)

## Copyright

Copyright (c) 2026 [Radio Bern RaBe](http://www.rabe.ch)
