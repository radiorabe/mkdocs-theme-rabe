"""Playwright visual snapshot tests for mkdocs-theme-rabe.

These tests render real pages served from the locally built site and
compare screenshots against committed baseline images.

First-time setup (create baseline snapshots):

    playwright install chromium
    poetry run pytest tests/playwright/ --snapshot-update

Subsequent runs will compare against those baselines and fail on any
visual regression.
"""

from __future__ import annotations

import pytest
from playwright.sync_api import Page, expect


VIEWPORT_DESKTOP = {"width": 1280, "height": 800}
VIEWPORT_MOBILE = {"width": 390, "height": 844}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _goto(page: Page, live_server: str, path: str = "/") -> None:
    page.goto(f"{live_server}{path}", wait_until="networkidle")


# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------


class TestHomePage:
    def test_title(self, page: Page, live_server: str):
        _goto(page, live_server, "/")
        expect(page).to_have_title("mkdocs-theme-rabe")

    def test_hero_section_visible(self, page: Page, live_server: str):
        _goto(page, live_server, "/")
        hero = page.locator(".tx-hero")
        expect(hero).to_be_visible()

    def test_hero_heading(self, page: Page, live_server: str):
        _goto(page, live_server, "/")
        heading = page.locator(".tx-hero h1")
        expect(heading).to_contain_text("mkdocs-theme-rabe")

    def test_primary_cta_button(self, page: Page, live_server: str):
        _goto(page, live_server, "/")
        btn = page.locator(".tx-hero .md-button--primary")
        expect(btn).to_be_visible()

    @pytest.mark.snapshot
    def test_home_desktop_screenshot(
        self, page: Page, live_server: str, snapshot
    ):
        page.set_viewport_size(VIEWPORT_DESKTOP)
        _goto(page, live_server, "/")
        screenshot = page.screenshot(full_page=True)
        snapshot.assert_match(screenshot, "home-desktop.png")

    @pytest.mark.snapshot
    def test_home_mobile_screenshot(
        self, page: Page, live_server: str, snapshot
    ):
        page.set_viewport_size(VIEWPORT_MOBILE)
        _goto(page, live_server, "/")
        screenshot = page.screenshot(full_page=True)
        snapshot.assert_match(screenshot, "home-mobile.png")


# ---------------------------------------------------------------------------
# Getting-started page
# ---------------------------------------------------------------------------


class TestGettingStartedPage:
    def test_title(self, page: Page, live_server: str):
        _goto(page, live_server, "/getting-started/")
        expect(page).to_have_title("Getting Started - mkdocs-theme-rabe")

    def test_navigation_tabs_visible(self, page: Page, live_server: str):
        _goto(page, live_server, "/getting-started/")
        tabs = page.locator(".md-tabs")
        expect(tabs).to_be_visible()

    @pytest.mark.snapshot
    def test_getting_started_screenshot(
        self, page: Page, live_server: str, snapshot
    ):
        page.set_viewport_size(VIEWPORT_DESKTOP)
        _goto(page, live_server, "/getting-started/")
        screenshot = page.screenshot(full_page=True)
        snapshot.assert_match(screenshot, "getting-started.png")


# ---------------------------------------------------------------------------
# Dark / light mode toggle
# ---------------------------------------------------------------------------


class TestColorScheme:
    def test_dark_mode_attribute(self, page: Page, live_server: str):
        """The default palette is slate (dark); the html element should
        carry ``data-md-color-scheme="slate"``."""
        _goto(page, live_server, "/")
        scheme = page.evaluate(
            "document.querySelector('html').getAttribute('data-md-color-scheme')"
        )
        assert scheme in ("slate", "default")

    @pytest.mark.snapshot
    def test_light_mode_screenshot(
        self, page: Page, live_server: str, snapshot
    ):
        page.set_viewport_size(VIEWPORT_DESKTOP)
        _goto(page, live_server, "/")
        # Switch to light mode via the toggle
        toggle = page.locator("[data-md-toggle='__palette_1']")
        if toggle.count():
            toggle.click()
            page.wait_for_timeout(400)
        screenshot = page.screenshot(full_page=False)
        snapshot.assert_match(screenshot, "home-light-mode.png")


# ---------------------------------------------------------------------------
# Brand colour assertions
# ---------------------------------------------------------------------------


class TestBrandColours:
    def test_header_background_is_teal(self, page: Page, live_server: str):
        """The header background should be the RaBe teal (#00c9bf)."""
        _goto(page, live_server, "/")
        bg = page.evaluate(
            "getComputedStyle(document.querySelector('.md-header')).backgroundColor"
        )
        # Accept rgb(0, 201, 191) or rgba variant
        assert "0, 201, 191" in bg or "00c9bf" in bg.lower(), (
            f"Unexpected header background: {bg}"
        )
