import csv
from datetime import datetime


def save_articles_to_csv(articles, filename_prefix="articles"):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{filename_prefix}_{date_str}.csv"

    fieldnames = ["title", "url", "points", "author", "comments"]

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for article in articles:
            writer.writerow(article)

    print(f"✅ Articles saved to {filename}")