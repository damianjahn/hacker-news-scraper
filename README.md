
# 📰 Hacker News Scraper

A simple Python web scraper for extracting top articles from [Hacker News](https://news.ycombinator.com/), built with `requests` and `BeautifulSoup`. Includes a PyTest test suite with mocked tests for common edge cases.

---

## 📦 Features

- Extracts:
  - Article title
  - URL
  - Points (upvotes)
  - Author
  - Comments count
- Keyword filtering (case-insensitive) with command line arguments
- Saves results to `.csv` file with date-based filename
- Includes unit tests with `pytest`
- Mocked tests for:
  - Missing points
  - Missing author
  - Empty page scenarios

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hacker-news-scraper.git
cd hacker-news-scraper
```

### 2. Set Up the Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🛠 Usage

Run the scraper manually:

### Without filtering (saves all articles):

```bash
python run_scraper.py
```

### With keyword filtering:

```bash
python run_scraper.py --keywords Python AI "Machine Learning"
```

### Custom output filename:

```bash
python run_scraper.py --keywords Python AI --output hacker_news_filtered
```

The results will be saved to a `.csv` file with the current date in the filename.

---

## ✅ Running Tests

```bash
pytest -s
```

The project includes both:
- Real scraper tests (live data)
- Mocked tests with custom HTML to ensure stability

---

## 📝 Project Structure

```
hacker-news-scraper/
├── scraper/            # Scraper logic
│   ├── hacker_news.py
│   ├── save_results.py
├── tests/              # PyTest test suite
│   ├── test_hacker_news.py
│   ├── test_save_results.py
│   └── test_filter.py
├── run_scraper.py      # Manual scraper runner with CLI
├── requirements.txt
└── README.md
```

---

## 📧 Future Ideas

- Automatically email yourself the scraped articles
- Schedule scraper to run weekly with `schedule` or `cron`
- Deploy as a small API with Flask or FastAPI

---

## ⚡ License

This project is for educational purposes. Scrape responsibly and respect target websites' policies.

---

## 🔧 Requirements

- Python 3.13
- `requests`
- `beautifulsoup4`
- `pytest`
- `argparse` (built-in)
