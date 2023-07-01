import requests
import webbrowser

API_KEY = '8573f8988b944356b4e5fe80b22586bc'
URL = ('https://newsapi.org/v2/top-headlines?')
CHROME_PATH ='C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def get_articles_by_category(category):
    query_paramters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_paramters)

def get_articles_by_source(source):
    query_parameters = {
        "sources": source,
        'apiKey': API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    print(results)

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')
        webbrowser.get(CHROME_PATH).open(result['url'])

#get_articles_by_category('technology')
get_articles_by_source('bbc-news')
