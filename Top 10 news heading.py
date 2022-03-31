# Read the news paper
import json

import requests

from win32com.client import Dispatch


def speak(given_str):
    tell = Dispatch("SAPI.spvoice")
    tell.Speak(given_str)


def latest_news():
    print("Please select your news category")
    speak("Please select your news category")
    category = ['business', 'entertainment', 'generalhealth', 'science', 'sports', 'technology']
    i = 0
    while i < 6:
        print(f"{i + 1} for {category[i]}")
        i = i + 1
    j = int(input())
    query_params = {
        "category": category[j - 1],
        "country": "in",
        "sortBy": "top",
        "apiKey": "b53cdda338124c74aeb1a3390f724785"
    }
    main_url = " https://newsapi.org/v2/top-headlines"
    news_req = requests.get(main_url, params=query_params).text
    news = json.loads(news_req)
    article = news['articles']
    print('To get the detail news you can click the link given below it')
    speak('To get the detail news you can click the link given below it')
    speak('first news is')
    for i in range(10):
        print(i + 1, article[i]['title'])
        print(f"To further read it visit {article[i]['url']}")
        speak(article[i]['title'])
        speak('Moving on to our next news')
    speak('Thank you for listening')


if __name__ == '__main__':
    latest_news()
