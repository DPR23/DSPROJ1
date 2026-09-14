# Real-Time News Sentiment Dashboard 📰

A Python-based web application that fetches live news headlines from Google News for any topic and performs natural language processing (NLP) to analyze the sentiment (Positive, Negative, Neutral) of each headline. 

This project demonstrates skills in data extraction, NLP, and interactive data visualization.

## Features
- **Live Data:** Fetches up-to-date headlines via Google News RSS.
- **NLP Sentiment Analysis:** Uses `TextBlob` to score the polarity and subjectivity of headlines.
- **Interactive Dashboard:** Built with `Streamlit` and `Plotly` to display sentiment distributions and data tables.

## Tech Stack
- **Python 3**
- **Streamlit** (Web framework)
- **Pandas** (Data manipulation)
- **TextBlob** (Sentiment Analysis)
- **Plotly** (Data Visualization)
- **Feedparser** (RSS parsing)

## Future Improvements
- Add advanced NLP models (e.g., HuggingFace Transformers/FinBERT) for more accurate financial sentiment.
- Add historical sentiment tracking by storing data in a database (e.g., SQLite/PostgreSQL).
- Deploy the application to Streamlit Community Cloud or Heroku.
