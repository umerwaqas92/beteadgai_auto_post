import time
from selenium import webdriver
import genrate_image as genrate_image
import os
import json
import post_insta
import post_to_facbook
from instagrapi import Client
from app_data.manage_app_config import get_config

def get_website_image(web_url):
    # Path to the ChromeDriver executable
    chromedriver_path = '/path/to/chromedriver'

    # URL of the website you want to capture
    website_url = web_url

    # Set up Chrome options with a user agent for a desktop device
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

    # Set the window size to emulate a desktop device
    window_width = 1024
    window_height = 1024
    chrome_options.add_argument(f'--window-size={window_width},{window_height}')

    # Create a new Chrome webdriver
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    # Open the website
    driver.get(website_url)

    # Wait for 5 seconds
    time.sleep(5)

    # Capture a screenshot
    screenshot_path = 'news/screenshot.png'
    driver.save_screenshot(screenshot_path)

    # Close the webdriver
    driver.quit()
    return screenshot_path


# path=get_website_image(web_url="https://monica.im/")
# title="Personal Al assistant for effortless chatting and copywriting."
# words = title.split()

# news_with_asterisks = []
# previous_word_length = 0

# for word in words:
#     if len(word) > 6 and previous_word_length <= 6:
#         news_with_asterisks.append("*" + word + "*")
#     else:
#         news_with_asterisks.append(word) 
#     previous_word_length = len(word)

# news_with_asterisks = " ".join(news_with_asterisks)

# # genrate_image.generate_news_image_from_path(path,news_with_asterisks)
# genrate_image.generate_news_image_potraite("https://images.pexels.com/photos/17445669/pexels-photo-17445669/free-photo-of-city-landscape-fashion-man.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",news_with_asterisks)


def get_astric_text(title):
   
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
    return news_with_asterisks

def check_product():
    product_data=[]
    with open("app_data/product_data.json", "r") as file:
        product_data = json.load(file)

    cl = Client()

    # Log in to your Instagram account
    username = get_config("insta_username")
    password = get_config("insta_password")

    cl.login(username=username, password=password)



        
    for product in product_data:
       web_img_path= get_website_image(web_url=product["url"])
       title=get_astric_text(product["title"])
       image_path=genrate_image.generate_news_image_from_path(web_img_path,title)
       image_stories=genrate_image.generate_news_image_potraite("",title,web_img_path)
       post_to_facbook.post_to_facebook(image_path,product["description"],product["url"])
       post_insta.post_insagram(cl,image_path,image_stories,product["description"],product["url"])
       



check_product()
