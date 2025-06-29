from Scraper.hacker_news import filter_articles_by_keywords

def test_filter_returns_only_matching_articles():
    articles = [
        {"title": "Learn Python in 10 Minutes"},
        {"title": "Latest News About AI"},
        {"title": "Some Random Article"},
    ]

    keywords = ["Python", "AI"]
    filtered = filter_articles_by_keywords(articles, keywords)

    assert len(filtered) == 2
    assert any("Python" in article["title"] for article in filtered)
    assert any("AI" in article["title"] for article in filtered)


def test_filter_is_case_insensitive():
    articles = [
        {"title": "Master machine learning techniques"},
        {"title": "Introduction to AI"},
    ]

    keywords = ["MACHINE", "ai"]
    filtered = filter_articles_by_keywords(articles, keywords)

    assert len(filtered) == 2


def test_filter_returns_empty_list_if_no_match():
    articles = [
        {"title": "Learn Cooking"},
        {"title": "Travel Tips"},
    ]

    keywords = ["Python", "AI"]
    filtered = filter_articles_by_keywords(articles, keywords)

    assert filtered == []