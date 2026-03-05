"""Unit tests for mkdocs_theme_rabe.hooks."""

from unittest.mock import MagicMock

import pytest

from mkdocs_theme_rabe.hooks import _get_version, on_page_context


@pytest.fixture()
def mock_page():
    page = MagicMock()
    page.is_homepage = False
    return page


@pytest.fixture()
def mock_config():
    return MagicMock()


@pytest.fixture()
def mock_nav():
    return MagicMock()


class TestOnPageContext:
    def test_injects_rabe_theme_key(self, mock_page, mock_config, mock_nav):
        context = {}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert "rabe_theme" in result

    def test_is_home_false_for_regular_page(
        self, mock_page, mock_config, mock_nav
    ):
        mock_page.is_homepage = False
        context = {}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert result["rabe_theme"]["is_home"] is False

    def test_is_home_true_for_homepage(self, mock_page, mock_config, mock_nav):
        mock_page.is_homepage = True
        context = {}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert result["rabe_theme"]["is_home"] is True

    def test_version_key_is_present(self, mock_page, mock_config, mock_nav):
        context = {}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert "version" in result["rabe_theme"]

    def test_existing_context_keys_are_preserved(
        self, mock_page, mock_config, mock_nav
    ):
        context = {"existing_key": "existing_value"}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert result["existing_key"] == "existing_value"

    def test_returns_context_dict(self, mock_page, mock_config, mock_nav):
        context = {}
        result = on_page_context(
            context, page=mock_page, config=mock_config, nav=mock_nav
        )
        assert result is context


class TestGetVersion:
    def test_returns_string(self):
        version = _get_version()
        assert isinstance(version, str)
        assert len(version) > 0
