
from instagrapi import Client
import time

# Create an instance of the bot
import app_data.manage_app_config as config
import get_tags as tags

def post_insagram(cl,photo_path,photo_story_path, message,comment):
    tags_list=tags.extract_tags(message)
    follow_msg="Visit www.BetEdge.ai for the most advanced betting edge."
    
    media = cl.photo_upload(
        photo_path,
        message+"\n\n"+follow_msg+"\n"+ tags_list,
        extra_data={
            "custom_accessibility_caption": "Artificially Intelligent News",
            "like_and_view_counts_disabled": 0,
            "disable_comments": 0,
        }
    )

    delay = 5
    time.sleep(delay)

    cl.photo_upload_to_story(photo_story_path)
    delay = 2

    # Upload the post
    result=media.dict()
    if(comment is not None or comment is not "" or comment is not "fluttydev"):
        comment = cl.media_comment(result["id"], comment)
        comment.dict()


    print(comment)
