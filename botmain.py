import json
import datetime
import random
import time
from newsapi import NewsApiClient
from genrate_image import *
from post_to_facbook import post_to_facebook
import os
from instagrapi import Client
from instadata.post_insta import post_insagram
from app_data.manage_app_config import * 

from app_data.news_model import MyNewsModel
import GoNewsGet 
import Newsapiorg
import worldnewsapi
import news_database as db
# Create an instance of the bot
from instadata.manageinsta import cl




articles = []


# go_news_list=GoNewsGet.GoNewsGet()
news_list=Newsapiorg.getNewAPIOrg(query="sports betting")
news_list2=Newsapiorg.getNewAPIOrg(query="sports")

for news in news_list2:
    news_list.append(news)

# worldnewsapi_news_list=worldnewsapi.search_news_worldnewsapi()

# for news in go_news_list:
#     articles.append(news)

for news in news_list:
    articles.append(news)


# for news in worldnewsapi_news_list:
#     articles.append(news)

        


print("total news got ",len(articles))



for article in articles:
    title = article.title
    
    if db.check_title_exists(title):
        # print("Skipping >>>>"+title)
        # print("Skipping >>>>"+blacklisted_titles)

        continue
    
    urlToImage = article.urlToImage
    description = article.description,
    url = article.url


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

        tags=""
    #    #get tags from title
        db.insert_article(title)

       
        
        # print("Title:", title)
        # print("Image:", article.urlToImage)
        # print("description:", article.description)
        # print("url:", article.url)


        file_name = generate_news_image(article.urlToImage, news_with_asterisks)
        # file_name_story=generate_news_image_potraite(article.urlToImage, news_with_asterisks,None)
       
        # print("file_name:", file_name)
        photo_id=post_to_facebook(file_name, article.description, article.url)
        # photo_id_story=post_insagram(file_name_story, article.description)
        # post_insagram(cl,file_name,file_name_story ,article.description, article.url)
        os.remove(file_name)
        # os.remove(file_name_story)



        
    
        delay = 60
        time.sleep(delay)

        # print("Title:", article.title)
        # print("Image:", article.description)
        # print("Image URL:", article.urlToImage)
        # print("source:", article.url)
        # print("------")

        # Save title and time in data list
       


    except Exception as e:
        print("Error "+str(e)+" while generating image for "+title)
       
        pass

# Save data to JSON file
