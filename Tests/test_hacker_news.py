import pytest
from Scraper.hacker_news import fetch_hacker_news
from unittest.mock import patch, Mock

def test_fetch_hacker_news_returns_list():
    articles = fetch_hacker_news()
    print(articles)
    assert isinstance(articles, list)
    assert len(articles) > 0
    for article in articles:
        assert "title" in article
        assert "url" in article
        assert "points" in article
        assert "author" in article
        assert "comments" in article

def test_article_structure():
    """ test that their structure and types are correct"""
    articles = fetch_hacker_news()
    first_article = articles[0]

    assert isinstance(first_article["title"], str)
    assert isinstance(first_article["url"], str)
    assert isinstance(first_article["points"], int)
    assert isinstance(first_article["author"], str)
    assert isinstance(first_article["comments"], str)

def test_article_points_non_negative():
    """test for sanity checks, like points never being negative"""
    articles = fetch_hacker_news()
    for article in articles:
        assert article["points"] >= 0

def test_article_urls_contain_http():
    """Test That URLs Are Valid-Looking"""
    articles = fetch_hacker_news()
    for article in articles:
        assert article["url"].startswith("http") or article["url"].startswith("item?id=")


MOCK_HTML = """
<html>
  <body>
    <tr class='athing'>
      <td class="title">
        <span class="titleline">
          <a href="https://example.com/article">Example Article</a>
        </span>
      </td>
    </tr>
    <tr>
      <td class="subtext">
        <span class="score">100 points</span>
        <a href="user?id=exampleuser" class="hnuser">exampleuser</a>
        <a href="item?id=12345">50 comments</a>
      </td>
    </tr>
  </body>
</html>
"""

@patch("Scraper.hacker_news.requests.get")
def test_fetch_hacker_news_with_mock(mock_get):
    """Mock test"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML
    mock_get.return_value = mock_response

    articles = fetch_hacker_news()

    assert len(articles) == 1
    article = articles[0]

    assert article["title"] == "Example Article"
    assert article["url"] == "https://example.com/article"
    assert article["points"] == 100
    assert article["author"] == "exampleuser"
    assert article["comments"] == "50 comments"

MOCK_HTML_MISSING_POINTS = """
<html>
  <body>
    <tr class='athing'>
      <td class="title">
        <span class="titleline">
          <a href="https://example.com/article">Article Without Points</a>
        </span>
      </td>
    </tr>
    <tr>
      <td class="subtext">
        <a href="user?id=exampleuser" class="hnuser">exampleuser</a>
        <a href="item?id=12345">25 comments</a>
      </td>
    </tr>
  </body>
</html>
"""

@patch("Scraper.hacker_news.requests.get")
def test_article_with_missing_points(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML_MISSING_POINTS
    mock_get.return_value = mock_response

    articles = fetch_hacker_news()
    assert len(articles) == 1
    article = articles[0]
    assert article["points"] == 0  # Default when points are missing

MOCK_HTML_MISSING_AUTHOR = """
<html>
  <body>
    <tr class='athing'>
      <td class="title">
        <span class="titleline">
          <a href="https://example.com/article">Article Without Author</a>
        </span>
      </td>
    </tr>
    <tr>
      <td class="subtext">
        <span class="score">50 points</span>
        <a href="item?id=12345">15 comments</a>
      </td>
    </tr>
  </body>
</html>
"""

@patch("Scraper.hacker_news.requests.get")
def test_article_with_missing_author(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML_MISSING_AUTHOR
    mock_get.return_value = mock_response

    articles = fetch_hacker_news()
    assert len(articles) == 1
    article = articles[0]
    assert article["author"] == "N/A"  # Default when author is missing

MOCK_HTML_EMPTY_PAGE = "<html><body></body></html>"

@patch("Scraper.hacker_news.requests.get")
def test_empty_page_returns_no_articles(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = MOCK_HTML_EMPTY_PAGE
    mock_get.return_value = mock_response

    articles = fetch_hacker_news()
    assert articles == []