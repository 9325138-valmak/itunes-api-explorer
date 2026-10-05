"""Data models for iTunes API responses."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SearchResult:
    artist: str
    track: str | None
    album: str | None
    media_type: str
    release_year: int | None
    price: float | None
    currency: str | None
    preview_url: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SearchResult:
        """Parse a raw iTunes API result dict into a SearchResult."""
        release_date = data.get("releaseDate", "")
        year: int | None = None
        if release_date and len(release_date) >= 4:
            try:
                year = int(release_date[:4])
            except ValueError:
                pass

        return cls(
            artist=data.get("artistName", "Unknown"),
            track=data.get("trackName"),
            album=data.get("collectionName"),
            media_type=data.get("kind", data.get("wrapperType", "unknown")),
            release_year=year,
            price=data.get("trackPrice") or data.get("collectionPrice"),
            currency=data.get("currency"),
            preview_url=data.get("previewUrl"),
        )
