# https://docs.python.org/3/library/json.html
# This library will be used to parse the JSON data returned by the API.
import json
# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request
import ssl
import app_data.manage_app_config as config
from app_data.news_model import MyNewsModel

ssl._create_default_https_context = ssl._create_unverified_context



category="Artificial%20Intelligence"


apikey = config.get_config("GoNewsGet")

def GoNewsGet():
    url = f"https://gnews.io/api/v4/search?q={category}&lang=en&apikey={apikey}&max=100"
    # print(url)
    list_of_news = []


    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
        

        for i in range(len(articles)):
            news_data=MyNewsModel(0,articles[i]["title"],articles[i]["content"],articles[i]["image"],articles[i]["url"] ,articles[i]["description"], )

            list_of_news.append(news_data)
            # articles[i].title
            # print(f"Title: {articles[i]['title']}")
            # # articles[i].description
            # print(f"Description: {articles[i]['description']}")
            # You can replace {property} below with any of the article properties returned by the API.
            # articles[i].{property}
            # print(f"{articles[i]['{property}']}")


    return list_of_news
       

# list=GoNewsGet()
# print(len(list))
