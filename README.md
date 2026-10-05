# iTunes API Client

A small Python client for the public [iTunes Search API](https://performance-partners.apple.com/search-api). It sends a search request, handles HTTP errors and timeouts, and parses the JSON response into typed data models.

Built as part of a data science curriculum (module on HTTP requests and APIs).

## What is in this repo

| Path | Purpose |
|---|---|
| `itunes_explorer/client.py` | HTTP client for the iTunes Search API |
| `itunes_explorer/models.py` | Dataclasses for search results |
| `tests/` | pytest tests that run against a recorded sample response, so no network is needed |
| `pyproject.toml` | Dependencies and tool config |

## Install

Requires Python 3.10 or newer.

```bash
git clone https://github.com/9325138-valmak/itunes-api-explorer
cd itunes-api-explorer
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Run the tests

```bash
pytest
```

## Roadmap

Not implemented yet:

- Command-line interface (`itunes search`, `itunes stats`)
- CSV export
- pandas summaries (release years, top artists, price ranges)

## License

MIT
