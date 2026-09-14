import feedparser
from textblob import TextBlob
import pandas as pd
from datetime import datetime
from email.utils import parsedate_to_datetime

def fetch_news(query, num_articles=20):
    """
    Fetches news from Google News RSS feed for a given query.
    """
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    
    articles = []
    for entry in feed.entries[:num_articles]:
        # Parse published date
        try:
            pub_date = parsedate_to_datetime(entry.published).strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            pub_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
        # Get sentiment
        sentiment, subjectivity = analyze_sentiment(entry.title)
        
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': pub_date,
            'source': entry.source.title if 'source' in entry else 'Unknown',
            'sentiment': sentiment,
            'subjectivity': subjectivity,
            'sentiment_category': categorize_sentiment(sentiment)
        })
        
    return pd.DataFrame(articles)

def analyze_sentiment(text):
    """
    Returns polarity (-1 to 1) and subjectivity (0 to 1) using TextBlob.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def categorize_sentiment(polarity):
    """
    Categorizes sentiment score into Positive, Negative, or Neutral.
    """
    if polarity > 0.05:
        return 'Positive'
    elif polarity < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    # Test the function
    df = fetch_news("Artificial Intelligence", 5)
    print(df.head())
