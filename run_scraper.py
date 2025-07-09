import argparse
from datetime import datetime
from Scraper.hacker_news import fetch_hacker_news, filter_articles_by_keywords
from Scraper.save_results import save_articles_to_csv
from Scraper.email_service import send_email

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hacker News Scraper with keyword filtering and email support")
    parser.add_argument(
        "--keywords",
        nargs="*",
        default=[],
        help="Keywords to filter article titles (case-insensitive). Example: --keywords Python AI"
    )
    parser.add_argument(
        "--output",
        default="articles",
        help="Output filename prefix (default: articles)"
    )
    parser.add_argument(
        "--email",
        action="store_true",
        help="Send an email with the results"
    )

    args = parser.parse_args()

    # Step 1: Scrape articles
    articles = fetch_hacker_news()

    # Step 2: Apply filtering (if any)
    if args.keywords:
        filtered_articles = filter_articles_by_keywords(articles, args.keywords)
        print(f"Total articles scraped: {len(articles)}")
        print(f"Articles matching keywords ({args.keywords}): {len(filtered_articles)}")
        articles_to_save = filtered_articles
    else:
        print(f"Total articles scraped: {len(articles)} (No filtering applied)")
        articles_to_save = articles

    # Step 3: Print results
    for idx, article in enumerate(articles_to_save, start=1):
        print(f"{idx}. {article['title']} ({article['url']})")
        print(f"   Points: {article['points']} | Author: {article['author']} | Comments: {article['comments']}\n")

    # Step 4: Save to file
    save_articles_to_csv(articles_to_save, filename_prefix=args.output)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{args.output}_{date_str}.csv"

    # Step 5: Optional email
    if args.email and articles_to_save:
        print("Sending email notification...")

        # Replace with your actual secure credentials
        sender_email = "your_email@example.com"
        receiver_email = "recipient_email@example.com"
        smtp_server = "smtp.gmail.com"
        smtp_port = 465
        smtp_password = "your_app_password"

        email_body = "\n\n".join(f"{a['title']} - {a['url']}" for a in articles_to_save)

        send_email(
            subject="Your Hacker News Articles",
            body=email_body,
            sender_email=sender_email,
            receiver_email=receiver_email,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            smtp_password=smtp_password,
            attachment_path=filename
        )