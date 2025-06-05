
# news_fetcher.py
import feedparser
import pandas as pd

def fetch_rss_headlines(feed_url="https://www.forexfactory.com/rss.php?f=2"):
    feed = feedparser.parse(feed_url)
    headlines = []
    for entry in feed.entries[:10]:  # Limit to latest 10 headlines
        headlines.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    return pd.DataFrame(headlines)

# Example usage:
# df = fetch_rss_headlines()
