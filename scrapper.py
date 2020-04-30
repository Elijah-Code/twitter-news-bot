import requests


def get_news(url):
    news = []
    counter = 0
    request = requests.get(url).json()
    articles = request['articles']
    while counter < len(articles):
        current = articles[counter]
        description = current['description']
        link = current['url']
        news.append((description, link))
        counter += 1
    return news
    # for num in articles:
    #     current = articles[num]
    #     description = current['description']
