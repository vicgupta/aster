import ast, base64, datetime, io, json, os, random, requests, time, urllib
from typing import Any, Dict, List, Literal, Optional, Tuple, Union
import requests

# Display mode enables printing of API requests and responses
display_requests = True 
display_responses = True

# Debug mode enables comprehensive logging for detailed diagnostics
debug_mode = False

# Define color codes
COLORS = {
    'cyan': '\033[96m',
    'blue': '\033[94m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'reset': '\033[0m'
}

def print_color(message, color):
    print(f"{COLORS.get(color, '')}{message}{COLORS['reset']}")

def print_api_request(message):
    if not display_requests:
        return
    print_color(message, 'cyan')

def print_api_response(message):
    if not display_responses:
        return
    print_color(message, 'blue')

def print_debug(message):
    if not debug_mode:
        return
    print_color(message, 'yellow')

def print_error(message):
    print_color(message, 'red')


class WebTools:

    @staticmethod
    def get_duckduckgo_search(query="chatgpt", region="us-en", safesearch="on", timeline="m", max_results=10, backend='api'):
        from duckduckgo_search import DDGS
        try:
            results = DDGS().text(query, region=region, safesearch=safesearch, timelimit=timeline, max_results=max_results, backend=backend)
            return results
        except Exception as e:
            print("An error occurred:", e)
            return None

    @staticmethod
    def get_duckduckgo_news(query="chatgpt", region="us-en", safesearch="on", timeline="m", max_results=10):
        from duckduckgo_search import DDGS
        try:
            results = DDGS().news(query, region=region, safesearch=safesearch, timelimit=timeline, max_results=max_results)
            return results
        except Exception as e:
            print("An error occurred:", e)
            return None

    @staticmethod
    def get_text_from_url(url):
        from bs4 import BeautifulSoup
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
            return text
        except Exception as e:
            print("An error occurred:", e)
            return None
            
    # pip install -U scikit-learn
    @staticmethod
    def calculate_cosine_similarity(text1, text2):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        texts = [text1, text2]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(texts)
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])    
        return cosine_sim[0][0]

