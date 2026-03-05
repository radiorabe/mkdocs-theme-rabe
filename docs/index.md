---
template: home.html
hero_cta_primary:
  text: Get Started
  url: getting-started/
hero_cta_secondary:
  text: View on GitHub
  url: https://github.com/radiorabe/mkdocs-theme-rabe
cards:
  - title: Single install
    icon: "📦"
    description: >-
      One pip install mkdocs-theme-rabe delivers MkDocs, Material theme,
      RaBe branding, and all required extensions — nothing else to configure.
    url: getting-started/installation/
  - title: RaBe brand built-in
    icon: "🎨"
    description: >-
      The #00c9bf teal palette, dark/light toggle, and custom CSS are applied
      automatically — no copy-paste of colour codes across repos.
    url: configuration/theme/
  - title: Backstage-ready
    icon: "🔌"
    description: >-
      TechDocs-compatible output works in the Backstage developer portal
      with no shadow-DOM breakage.
    url: configuration/backstage/
  - title: Auto dark mode
    icon: "🌙"
    description: >-
      Slate (dark) and default (light) palette schemes with a toggle button
      are bundled as theme defaults — consumers opt in for free.
---

# mkdocs-theme-rabe

`mkdocs-theme-rabe` is a centralised MkDocs theme for all
[Radio Bern RaBe](https://rabe.ch) GitHub repositories.
It bundles the **RaBe brand identity**, common dependencies, and custom
rendering logic so every project automatically looks and feels consistent.

## Why?

Prior to this package, every RaBe repo carried its own `mkdocs.yml` full of
copy-pasted colour codes, extension lists, and CI steps.  Any branding
update required touching dozens of repositories.

With `mkdocs-theme-rabe`, you install a single package and get:

| Feature | Details |
|---|---|
| **RaBe colours** | `#00c9bf` teal primary / accent applied globally |
| **Material base** | Full MkDocs-Material feature set available |
| **Bundled deps** | `mkdocstrings`, `pymdown-extensions`, and more |
| **Backstage** | TechDocs-compatible output (no shadow-DOM breakage) |
| **Dark mode** | Slate + default palette toggle included |
