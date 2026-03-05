# Repository Modes

`mkdocs-theme-rabe` is intentionally generic, but the recommended plugin
stacks differ depending on the type of repository.

## Code / Python project

For Python packages that want auto-generated API docs:

```yaml title="mkdocs.yml"
plugins:
  - search
  - section-index
  - mkdocstrings:
      handlers:
        python:
          options:
            show_source: true
```

## Specification / documentation-only

For repos that are purely documentation (e.g. CRID Spec, container images):

```yaml title="mkdocs.yml"
plugins:
  - search
  - section-index
```

## README mirror

For simple single-page sites that mirror a `README.md`:

```yaml title="mkdocs.yml"
docs_dir: .         # read docs from the repo root
nav:
  - Home: README.md

plugins:
  - search
```

## Backstage / TechDocs

See the dedicated [Backstage integration guide](backstage.md).
