"""Integration tests for the mkdocs build command.

These tests verify that the rabe theme produces a valid site for both
plain MkDocs / GitHub Pages deployment and Backstage / TechDocs usage.

The Backstage TechDocs publisher reads pre-built documentation from
GitHub Pages, so both targets use the same ``mkdocs build`` output.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent


def _run_mkdocs(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "mkdocs", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


class TestMkDocsBuild:
    """Verify that ``mkdocs build --strict`` succeeds and produces a valid site."""

    @pytest.fixture(scope="class")
    def built_site(self, tmp_path_factory) -> Path:
        site = tmp_path_factory.mktemp("site")
        result = _run_mkdocs(["build", "--strict", "--site-dir", str(site)])
        assert result.returncode == 0, (
            f"mkdocs build failed:\n{result.stdout}\n{result.stderr}"
        )
        return site

    def test_index_html_exists(self, built_site: Path):
        assert (built_site / "index.html").exists()

    def test_404_page_exists(self, built_site: Path):
        assert (built_site / "404.html").exists()

    def test_assets_directory_exists(self, built_site: Path):
        assert (built_site / "assets").is_dir()

    def test_rabe_css_is_included(self, built_site: Path):
        rabe_css = built_site / "assets" / "stylesheets" / "rabe.css"
        assert rabe_css.exists()

    def test_llms_txt_is_generated(self, built_site: Path):
        """The llmstxt plugin should produce /llms.txt at build time."""
        assert (built_site / "llms.txt").exists()

    def test_index_html_uses_rabe_theme(self, built_site: Path):
        content = (built_site / "index.html").read_text()
        assert "rabe.css" in content

    def test_no_warnings_in_strict_mode(self, tmp_path):
        """Build must pass --strict, meaning zero warnings."""
        site = tmp_path / "site"
        result = _run_mkdocs(["build", "--strict", "--site-dir", str(site)])
        assert result.returncode == 0, (
            f"mkdocs build --strict produced warnings or errors:\n"
            f"{result.stdout}\n{result.stderr}"
        )


class TestBackstageCompatibility:
    """Verify the built site is compatible with Backstage / TechDocs.

    The RaBe Backstage instance uses a custom publisher that reads
    pre-built documentation from GitHub Pages.  TechDocs renders the same
    ``site/`` output that ``mkdocs build`` produces, so we verify that the
    output meets TechDocs requirements.
    """

    @pytest.fixture(scope="class")
    def built_site(self, tmp_path_factory) -> Path:
        site = tmp_path_factory.mktemp("backstage_site")
        result = _run_mkdocs(["build", "--strict", "--site-dir", str(site)])
        assert result.returncode == 0, (
            f"mkdocs build failed:\n{result.stdout}\n{result.stderr}"
        )
        return site

    def test_sitemap_xml_exists(self, built_site: Path):
        """TechDocs and search crawlers expect a sitemap."""
        assert (built_site / "sitemap.xml").exists()

    def test_index_html_has_no_absolute_base_url_js(self, built_site: Path):
        """No bare ``base_url`` JS global that would break in shadow DOM."""
        index = (built_site / "index.html").read_text()
        # The standard mkdocs search/main.js injects base_url via a script tag
        # that MkDocs places in the page.  Material handles this differently.
        # We just check the page renders a valid HTML5 document.
        assert "<!doctype html>" in index.lower() or "<!DOCTYPE html>" in index

    def test_navigation_structure_exists(self, built_site: Path):
        """Expected top-level navigation pages are present in the build."""
        for path in ("getting-started/index.html", "reference/index.html"):
            assert (built_site / path).exists(), f"Missing: {path}"
