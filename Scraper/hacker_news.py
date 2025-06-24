import requests
from bs4 import BeautifulSoup

HACKER_NEWS_URL = "https://news.ycombinator.com/"

def fetch_hacker_news():
    response = requests.get(HACKER_NEWS_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    items = soup.select(".athing")

    for item in items:
        title_tag = item.select_one(".titleline a")
        if not title_tag:
            continue

        title = title_tag.text
        url = title_tag["href"]

        subtext = item.find_next_sibling("tr").select_one(".subtext")
        points_tag = subtext.select_one(".score")
        author_tag = subtext.select_one(".hnuser")
        comments_tag = subtext.select("a")[-1] if subtext.select("a") else None

        points = int(points_tag.text.replace(" points", "")) if points_tag else 0
        author = author_tag.text if author_tag else "N/A"
        comments = comments_tag.text if comments_tag and "comment" in comments_tag.text else "0 comments"

        articles.append({
            "title": title,
            "url": url,
            "points": points,
            "author": author,
            "comments": comments
        })

    return articles