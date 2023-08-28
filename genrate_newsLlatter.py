import json
import random
from newsapi import NewsApiClient
from genrate_image import generate_news_image
from post_to_facbook import post_to_facebook
import os
from genrate_image_text import generate_image_text
from put_title_and_footer import *
from make_image_to_pdf import save_carousel_images_as_pdf
import datetime
from app_data.manage_app_config import *





category=get_config("news_article_category")


newsapi = NewsApiClient(api_key=get_config("news_api_key"))





time_from = datetime.datetime.now() - datetime.timedelta(days=7)
time_from_str = time_from.strftime("%Y-%m-%d")

time_from= datetime.datetime.now() - datetime.timedelta(days=7).strftime("%Y-%m-%d")
time_to= datetime.datetime.now().strftime("%Y-%m-%d")


time_from = datetime.datetime.now() - datetime.timedelta(days=7)
time_from_str = time_from.strftime("%Y-%m-%d")

time_to = datetime.datetime.now()
time_to_str = time_to.strftime("%Y-%m-%d")
                               
top_headlines = newsapi.get_everything(q=category, 
                                       language='en',
                                       from_param= time_from_str, 
                                       to= time_to_str
                                       )

articles = top_headlines["articles"]

data = []

limit = 2

blacklisted_titles = []

with open("app_data/data.json", "r") as file:
    data_json = json.load(file)
    for item in data_json:
        data.append(item)
        blacklisted_titles.append(item["title"])

for article in articles:
    title = article['title']
    
    if title in blacklisted_titles:
        print("Skipping >>>>"+title)
        continue
    
    urlToImage = article['urlToImage']
    description = article['description']
    url = article['url']


    words = title.split()

    news_with_asterisks = []
    previous_word_length = 0

    for word in words:
        if len(word) > 6 and previous_word_length <= 6:
            news_with_asterisks.append("*" + word + "*")
        else:
            news_with_asterisks.append(word)
        previous_word_length = len(word)

    news_with_asterisks = " ".join(news_with_asterisks)

    try:
        # Generate a random delay between 1 and 5 seconds
        print("Generating image..."+ title)
        file_name = generate_news_image(urlToImage, news_with_asterisks)
        file_name_text = generate_image_text(news_with_asterisks,article["description"])
      

        
        if(True):
            print("Title:", title)
            print("description:", article["description"])
            print("Image URL:", article["urlToImage"])
            print("source:", article["urlToImage"])
            print("content:", article["content"])

            print("------")

            # Save title and time in data list
            # data.append({
            #     "title": title,
            #     "time": datetime.datetime.now().isoformat()
            # })
            with open("app_data/data.json", "w") as file:
                json.dump(data, file, indent=2, separators=(",", ": "))  # Save data with indentation and separators


    except:
        pass


add_timestamp_to_image(category=category)
save_carousel_images_as_pdf(category=category)

# Save data to JSON file
