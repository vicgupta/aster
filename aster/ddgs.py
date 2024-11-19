# pip install -U duckduckgo_search==5.3.1
import random
from aster.tools import WebTools
import datetime as dt
from time import sleep

def get_ddgs_results(keyword:str = None, max_results:int = 10, timeline="w") -> list:
    results = []
    search_results = WebTools.get_duckduckgo_search(keyword, region="wt-wt", safesearch="on", timeline=timeline, max_results=max_results)
    for item in search_results:
        data = {'keyword': keyword,
                'date_created': dt.date.today().strftime("%Y-%m-%d"),
                'title': item['title'],
                'url': item['href'],
                'body': item['body']}
        # print (data)
        results.append(data)
    sleep(random.randint(10,20))

    news_results = WebTools.get_duckduckgo_news(keyword, region="wt-wt", safesearch="on", timeline="w", max_results=max_results)
    for item in news_results:
        data = {'keyword': keyword,
                'date_created': dt.date.today().strftime("%Y-%m-%d"),
                'title': item['title'],
                'url': item['url'],
                'body': item['body']}
            # print (data)
        results.append(data)
    sleep(random.randint(10,20))
    
    return results
