# from instagrapi.types import StoryMention, StoryMedia
# from instagrapi.story import StoryBuilder
# from instagrapi import Client
# import app_data.manage_app_config as config
# import time

# cl = Client()

# username = config.get_config("insta_username")
# password = config.get_config("insta_password")

# print(username)
# print(password)



# cl.login(username, password)


# # buildout = StoryBuilder('news/stories/At_the_heart_01.jpg').photo()

# # cl.video_upload_to_story(buildout.path)



# # cl.photo_upload_to_story('news/stories/At_the_heart_01.jpg')




from instagrapi import Client

cl = Client()
cl.login("artificiallyintelligentnews_92", "234")

