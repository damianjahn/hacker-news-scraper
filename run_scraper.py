import argparse
from Scraper.hacker_news import fetch_hacker_news, filter_articles_by_keywords
from Scraper.save_results import save_articles_to_csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hacker News Scraper with optional keyword filtering")
    parser.add_argument(
        "--keywords",
        nargs="*",
        default=[],
        help="List of keywords to filter articles by (case-insensitive). Example: --keywords Python AI"
    )
    parser.add_argument(
        "--output",
        default="articles",
        help="Output filename prefix (default: articles)"
    )

    args = parser.parse_args()

    articles = fetch_hacker_news()

    if args.keywords:
        filtered_articles = filter_articles_by_keywords(articles, args.keywords)
        print(f"Total articles scraped: {len(articles)}")
        print(f"Articles matching keywords ({args.keywords}): {len(filtered_articles)}")
        articles_to_save = filtered_articles
    else:
        print(f"Total articles scraped: {len(articles)} (No filtering applied)")
        articles_to_save = articles

    for idx, article in enumerate(articles_to_save, start=1):
        print(f"{idx}. {article['title']} ({article['url']})")
        print(f"   Points: {article['points']} | Author: {article['author']} | Comments: {article['comments']}\n")

    save_articles_to_csv(articles_to_save, filename_prefix=args.output)