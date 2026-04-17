"""Tests for the iTunes API client."""

import json
from pathlib import Path

import pytest
import responses as rsps

from itunes_explorer.client import ItunesAPIError, search
from itunes_explorer.models import SearchResult

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


@rsps.activate
def test_returns_list_of_search_results() -> None:
    fixture = load_fixture("sample_response.json")
    rsps.add(rsps.GET, "https://itunes.apple.com/search", json=fixture)
    results = search("Pink Floyd")
    assert isinstance(results, list)
    assert all(isinstance(r, SearchResult) for r in results)


@rsps.activate
def test_result_fields_are_parsed() -> None:
    fixture = load_fixture("sample_response.json")
    rsps.add(rsps.GET, "https://itunes.apple.com/search", json=fixture)
    results = search("Pink Floyd")
    first = results[0]
    assert first.artist
    assert first.release_year is None or isinstance(first.release_year, int)


@rsps.activate
def test_raises_on_http_error() -> None:
    rsps.add(rsps.GET, "https://itunes.apple.com/search", status=500)
    with pytest.raises(ItunesAPIError, match="HTTP 500"):
        search("anything")


@rsps.activate
def test_raises_on_malformed_json() -> None:
    rsps.add(
        rsps.GET,
        "https://itunes.apple.com/search",
        body='{"no_results_key": []}',
    )
    with pytest.raises(ItunesAPIError, match="Unexpected response format"):
        search("anything")


def test_raises_on_invalid_limit() -> None:
    with pytest.raises(ValueError, match="limit must be 1–200"):
        search("test", limit=0)

    with pytest.raises(ValueError, match="limit must be 1–200"):
        search("test", limit=201)
