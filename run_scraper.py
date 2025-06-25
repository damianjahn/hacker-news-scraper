from Scraper.hacker_news import fetch_hacker_news
from Scraper.save_results import save_articles_to_csv

if __name__ == "__main__":
    articles = fetch_hacker_news()

    for idx, article in enumerate(articles, start=1):
        print(f"{idx}. {article['title']} ({article['url']})")
        print(f"   Points: {article['points']} | Author: {article['author']} | Comments: {article['comments']}\n")

    save_articles_to_csv(articles)