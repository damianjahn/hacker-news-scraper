import os
import tempfile
from datetime import datetime
from Scraper.save_results import save_articles_to_csv


def test_save_articles_to_csv_creates_file():
    articles = [
        {
            "title": "Test Article",
            "url": "https://example.com",
            "points": 42,
            "author": "testuser",
            "comments": "15 comments"
        }
    ]

    with tempfile.TemporaryDirectory() as tmpdirname:
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename_prefix = os.path.join(tmpdirname, "test_articles")

        save_articles_to_csv(articles, filename_prefix=filename_prefix)

        expected_filename = f"{filename_prefix}_{date_str}.csv"

        assert os.path.exists(expected_filename)

        with open(expected_filename, "r", encoding="utf-8") as file:
            content = file.read()

        assert "Test Article" in content
        assert "https://example.com" in content
        assert "testuser" in content