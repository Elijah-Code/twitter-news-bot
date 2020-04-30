from twython import Twython
import auth
import scrapper
import time

url = 'http://newsapi.org/v2/top-headlines?country=us&apiKey=a30440902cbe4ed099dbf8b02fa7f7a7'
headlines = scrapper.get_news(url)
tweeted = []

twitter = Twython(
    auth.consumer_key,
    auth.consumer_secret,
    auth.access_token,
    auth.access_token_secret
)


def tweet():

    counter = 0
    while counter < len(headlines):
        description = headlines[counter][0]
        link = headlines[counter][1]
        if link not in tweeted:
            message = f"{description}\n{link}"  # tweet news
            twitter.update_status(status=message)
            print(f"Tweeted: {message}")
            counter += 1
            tweeted.append(link)
            time.sleep(3600)
        else:
            counter += 1


if __name__ == '__main__':
    tweet()
