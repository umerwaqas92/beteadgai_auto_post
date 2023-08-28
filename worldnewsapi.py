import ssl
import app_data.manage_app_config as config
from app_data.news_model import MyNewsModel
import app_data.manage_app_config  as  config

ssl._create_default_https_context = ssl._create_unverified_context

import requests

def search_news_worldnewsapi(search_text="artificial intelligence"):
    #https://api.worldnewsapi.com/

    api_key='fd5bc398aad94982b029594d840e8497',
    search_text=config.get_config("q")
    url = f"https://api.worldnewsapi.com/search-news?api-key={api_key}&text={search_text}"
    response = requests.get(url)
    list_of_news = []
    if response.status_code == 200:
        data = response.json()
        articles = data.get('news')
       
        for article in articles:
            try:
                title = article.get('title')
                description = article.get('text')
                image_url = article.get('image')
                url = article.get('url')
                news_data=MyNewsModel(news_id=0,title=title,content=description,image=image_url,url=url ,description=description )

                list_of_news.append(news_data)
                
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Image: {image_url}")
                print(f"URL: {url}")
            except:
                print("Error occurred while fetching news")
              
                # print("Error occurred
    else:
        print("Error occurred while fetching news:", response.status_code)

    return list_of_news


# data=search_news_worldnewsapi()
# print(len(data))
