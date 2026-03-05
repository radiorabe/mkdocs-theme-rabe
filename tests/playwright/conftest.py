"""Playwright fixtures for visual snapshot tests.

Run the full suite:

    poetry install
    playwright install chromium
    poetry run pytest tests/playwright/ --snapshot-update  # first run: create snapshots
    poetry run pytest tests/playwright/                    # subsequent runs: compare

The ``site`` directory is built once per session via the ``built_site``
fixture.
"""

from __future__ import annotations

import subprocess
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent
SITE_DIR = REPO_ROOT / "site"


@pytest.fixture(scope="session")
def built_site():
    """Build the MkDocs site exactly once for the whole test session."""
    subprocess.run(
        ["mkdocs", "build", "--strict"],
        cwd=REPO_ROOT,
        check=True,
    )
    return SITE_DIR


@pytest.fixture(scope="session")
def live_server(built_site):
    """Serve the built site on a random port for the duration of the session."""
    handler = _make_handler(built_site)
    server = HTTPServer(("127.0.0.1", 0), handler)
    port = server.server_address[1]

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    base_url = f"http://127.0.0.1:{port}"
    yield base_url

    server.shutdown()


def _make_handler(directory: Path):
    class _Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

    def log_message(self, *args) -> None:
        """Suppress request logs during tests."""

    return _Handler
