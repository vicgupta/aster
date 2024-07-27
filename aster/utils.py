def create_prompt(role: str, content: str):
    args = {"role": role, "content": content}
    return {**args}

# pip install requests beautifulsoup4
from bs4 import BeautifulSoup
import requests
def get_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    except Exception as e:
        print("An error occurred:", e)
        return None

# pip install duckduckgo-search
from duckduckgo_search import DDGS
def duckduckgo_search(query="chatgpt", region="us-en", safesearch="on", timeline="m", max_results=10):
    # returns results['title'], ['href'], ['body']
    try:
        results = DDGS().text(query, region=region, safesearch=safesearch, timelimit=timeline, max_results=max_results)
        return results
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
# results = duckduckgo_search(query="chatgpt", max_results=5)
# print (results)
