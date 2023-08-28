from newsapi import NewsApiClient
import app_data.manage_app_config as config
from app_data.news_model import MyNewsModel

def getNewAPIOrg():
    list_of_news = []

    newsapi = NewsApiClient(api_key=config.get_config("news_api_key"))

    top_headlines = newsapi.get_everything(q=config.get_config("q"))
    articles = top_headlines["articles"]

    for article in articles:
        news_instance = MyNewsModel(0,article['title'], article['content'],  article['urlToImage'],article['url'], article['description'])
        list_of_news.append(news_instance)

    return list_of_news

# news_list = getNewAPIOrg()
# print(len(news_list))
