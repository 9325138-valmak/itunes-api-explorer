"""iTunes Search API client."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

import requests

from itunes_explorer.models import SearchResult

BASE_URL = "https://itunes.apple.com/search"
DEFAULT_TIMEOUT = 10


class ItunesAPIError(Exception):
    pass


def search(
    term: str,
    media: str = "music",
    limit: int = 25,
    country: str = "US",
) -> list[SearchResult]:
    """Search the iTunes catalogue.

    Args:
        term: Search keyword(s)
        media: Media type — 'music', 'podcast', 'audiobook', 'all'
        limit: Maximum number of results (1–200)
        country: Two-letter ISO country code

    Returns:
        List of SearchResult objects

    Raises:
        ItunesAPIError: On HTTP error or malformed response
        ValueError: If limit is out of range
    """
    if not 1 <= limit <= 200:
        raise ValueError(f"limit must be 1–200, got {limit}")

    params: dict[str, Any] = {
        "term": term,
        "media": media,
        "limit": limit,
        "country": country,
    }
    url = f"{BASE_URL}?{urlencode(params)}"

    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()
    except requests.Timeout:
        raise ItunesAPIError(f"Request timed out after {DEFAULT_TIMEOUT}s")
    except requests.HTTPError as exc:
        raise ItunesAPIError(f"HTTP {exc.response.status_code}: {exc}") from exc
    except requests.RequestException as exc:
        raise ItunesAPIError(f"Request failed: {exc}") from exc

    try:
        data = response.json()
        results = data["results"]
    except (KeyError, ValueError) as exc:
        raise ItunesAPIError(f"Unexpected response format: {exc}") from exc

    return [SearchResult.from_dict(item) for item in results]
