import requests

def letestsnews():
    url =  "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=378bb5ff8391497a8adcca2d4b685ca7"
    r = requests.get(url)
    data = r.json()

    articles = data["articles"]
    for article in articles:
        title = article["title"]
        news_url = article["url"]
        print(f"Title: {title}")
        print(f"URL: {news_url}")