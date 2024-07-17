from flask import Flask, render_template, request
from models.news_api import NewsApiClient
from utils.config import config

app = Flask(__name__)

# Retrieve the API key from the config
news_api_key = config()['NEWS_API_KEY']
if not news_api_key:
    raise ValueError("NEWS_API_KEY not found in config")

# Initialize NewsApiClient with the API key
newsapi = NewsApiClient(api_key=news_api_key)

@app.route('/')
def index():
    try:
        # Fetch top headlines
        top_headlines = newsapi.get_top_headlines(country="in", language="en")
        total_results = top_headlines['totalResults']
        if total_results > 100:
            total_results = 100
        all_headlines = newsapi.get_top_headlines(country="in", language="en", page_size=total_results)['articles']
        return render_template('index.html', all_headlines=all_headlines)
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/search', methods=['POST'])
def search():
    try:
        # Get search query from form
        query = request.form['query']
        # Fetch articles based on the query
        all_articles = newsapi.get_everything(q=query, language="en", page_size=100)['articles']
        return render_template('search.html', all_articles=all_articles)
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
