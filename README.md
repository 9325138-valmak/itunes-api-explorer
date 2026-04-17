# 🎵 iTunes API Explorer

A command-line tool to search and analyse the iTunes catalogue. Demonstrates HTTP request handling, JSON parsing, and pandas-based data summarisation.

Built as part of a data science curriculum (Module 13 — HTTP requests and APIs).

## Features

- Search artists, albums, or tracks by keyword
- Filter results by media type (`music`, `podcast`, `audiobook`)
- Display results as a formatted table
- Export results to CSV for further analysis
- Summary statistics: release year distribution, top artists, price ranges

## Demo

```bash
# Search for tracks
itunes search "Pink Floyd" --media music --limit 20

# Export to CSV
itunes search "jazz" --media music --export results.csv

# Show summary stats for a search
itunes stats "Beatles" --media music
```

**Example output:**

```
Artist              Track                      Year    Price
------------------  -------------------------  ------  -------
Pink Floyd          Comfortably Numb           1979    $1.29
Pink Floyd          Wish You Were Here         1975    $1.29
Pink Floyd          Money                      1973    $1.29
...

Summary: 20 results | Years: 1973–1994 | Avg price: $1.29
```

## Setup

```bash
git clone https://github.com/valentin-makarov/itunes-api-explorer
cd itunes-api-explorer
pip install -e ".[dev]"
```

## Usage

```bash
itunes search QUERY [--media TYPE] [--limit N] [--export FILE]
itunes stats  QUERY [--media TYPE] [--limit N]
itunes --help
```

## Project Structure

```
itunes-api-explorer/
├── itunes_explorer/
│   ├── __init__.py
│   ├── cli.py          # argparse entry point
│   ├── client.py       # iTunes API HTTP client
│   ├── models.py       # dataclasses for API results
│   └── analysis.py     # pandas summarisation
├── tests/
│   ├── test_client.py
│   ├── test_models.py
│   └── fixtures/
│       └── sample_response.json
├── pyproject.toml
└── README.md
```

## Running Tests

```bash
pytest
pytest -v --tb=short
```

## What I Learned

- Handling HTTP errors and timeouts gracefully with `requests`
- Parsing nested JSON into typed dataclasses
- Using `pandas` for quick group-by summaries and CSV export
- Structuring a project with a proper CLI entry point

## License

MIT
