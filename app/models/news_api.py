import requests
from utils.config import config  # Adjusted import path

class NewsApiClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_headlines(self, country, language, page_size=100):
        url = f"https://newsapi.org/v2/top-headlines?country={country}&language={language}&apiKey={self.api_key}"
        response = requests.get(url)
        return response.json()

    def get_everything(self, q, language, page_size=100):
        url = f"https://newsapi.org/v2/everything?q={q}&language={language}&apiKey={self.api_key}"
        response = requests.get(url)
        return response.json()
