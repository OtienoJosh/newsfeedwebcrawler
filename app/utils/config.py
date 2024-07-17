import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def config():
    return {
        'NEWS_API_KEY': os.getenv('NEWS_API_KEY')
    }
