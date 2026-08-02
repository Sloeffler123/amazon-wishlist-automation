# Amazon Deal Finder

A tool that scrapes product listings from an Amazon page, pulls historical pricing data for each item, and flags which ones are actually good deals right now — instead of relying on the "% off" badge alone.

## What it does

- **Scrapes product ASINs** from a given Amazon page using Selenium, scrolling through the full page (infinite scroll) to collect every listed item, not just what's initially visible
- **Pulls price history** for each product from the [Keepa API](https://keepa.com/), including current, min, max, and 365-day average price
- **Calculates a "deal score"** — where the current price sits between the historical min and max — so you can tell a real discount from a routine price fluctuation
- **Exports results to CSV** with pandas, ready to sort/filter in a spreadsheet

## Why I built it

Amazon's own "deal" labeling doesn't account for a product's actual price history — something can be "20% off" while still priced higher than its typical price six months ago. This checks the real history instead of trusting the badge.

## Tech stack

| Layer | Tools |
|---|---|
| Scraping | Selenium |
| Price history | Keepa API |
| Data processing | pandas |
| Config | python-dotenv (API key stored in `.env`, not committed) |
| Testing | pytest |

## Project structure

```
main.py            # entry point — scrape, then query Keepa, then export
setup.py            # Chrome/Selenium driver configuration
harvest.py           # scrolls the page and collects ASINs into data_file.txt
keepa_api.py          # queries Keepa, calculates deal scores, writes CSV
test_keepa_funcs.py    # pytest coverage for price conversion & deal-scoring logic
```

## Testing

The core calculation logic — currency conversion and deal-score calculation — is covered by pytest with explicit input/output cases, including an edge case for products with no price history. This logic is tested independently of the live scraping/API calls, so it runs fast and doesn't depend on network access.

## Setup

1. Install dependencies:
   ```bash
   pip install selenium pandas keepa python-dotenv
   ```
2. Create a `.env` file with your Keepa API key:
   ```
   KEEPA_API_KEY=your_key_here
   AMAZON_URL=https://www.amazon.com/your-target-page
   ```
3. Run it:
   ```bash
   python main.py
   ```
4. Results land in `main_csv_data.csv`.

## Possible next steps

- Fix the `main_loop` exception handling so a failed lookup on the very first item doesn't throw an `UnboundLocalError`
- Make the Chrome user-data directory path cross-platform instead of hardcoded to Windows
- Add a proper `if __name__ == "__main__":` guard to `main.py`
