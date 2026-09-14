import streamlit as st
import plotly.express as px
from news_fetcher import fetch_news

st.set_page_config(page_title="Real-Time News Sentiment Dashboard", layout="wide")

st.title("📰 Real-Time News Sentiment Dashboard")
st.markdown("""
This dashboard fetches the latest news headlines from Google News for any topic you search for, 
and uses Natural Language Processing (NLP) to analyze the sentiment of each headline (Positive, Negative, or Neutral).
""")

# Sidebar for user inputs
st.sidebar.header("Search Parameters")
query = st.sidebar.text_input("Enter a topic or company name", value="Artificial Intelligence")
num_articles = st.sidebar.slider("Number of articles to fetch", min_value=10, max_value=100, value=30, step=10)

if st.sidebar.button("Fetch and Analyze News"):
    with st.spinner(f"Fetching news for '{query}'..."):
        df = fetch_news(query, num_articles)
        
        if df.empty:
            st.error("No news found for this topic. Try another search.")
        else:
            # Layout the top metrics
            col1, col2, col3 = st.columns(3)
            pos_count = len(df[df['sentiment_category'] == 'Positive'])
            neg_count = len(df[df['sentiment_category'] == 'Negative'])
            neu_count = len(df[df['sentiment_category'] == 'Neutral'])
            
            col1.metric("Positive Headlines", pos_count)
            col2.metric("Negative Headlines", neg_count)
            col3.metric("Neutral Headlines", neu_count)
            
            # Create charts
            st.subheader("Sentiment Distribution")
            
            # Pie Chart
            fig_pie = px.pie(
                df, 
                names='sentiment_category', 
                title='Sentiment Breakdown',
                color='sentiment_category',
                color_discrete_map={'Positive': 'green', 'Negative': 'red', 'Neutral': 'gray'}
            )
            
            # Scatter Plot (Polarity vs Subjectivity)
            fig_scatter = px.scatter(
                df, 
                x='sentiment', 
                y='subjectivity', 
                color='sentiment_category',
                hover_data=['title', 'source'],
                title='Sentiment Polarity vs Subjectivity',
                labels={'sentiment': 'Polarity (-1 to 1)', 'subjectivity': 'Subjectivity (0 to 1)'},
                color_discrete_map={'Positive': 'green', 'Negative': 'red', 'Neutral': 'gray'}
            )
            
            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                st.plotly_chart(fig_pie, use_container_width=True)
            with chart_col2:
                st.plotly_chart(fig_scatter, use_container_width=True)
                
            # Data table
            st.subheader("Recent Headlines")
            
            # Display colored dataframe
            def color_sentiment(val):
                color = 'green' if val == 'Positive' else 'red' if val == 'Negative' else 'gray'
                return f'color: {color}'
                
            st.dataframe(
                df[['published', 'title', 'source', 'sentiment_category', 'sentiment']]
                .style.map(color_sentiment, subset=['sentiment_category'])
            )
