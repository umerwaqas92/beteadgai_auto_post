import facebook
import app_data.manage_app_config as config
import get_tags as tags


def post_to_facebook(photo_path, message,comment):

# Replace these with your actual values
    page_id = '61550840662657'
    access_token = 'EAAJni6rVfXABOyG9SDHjZCZAn1dtPDghQtsKFt3iWJ9oVjOKVNw7aHZB39WgUpbRyvH8Ci61ZB8VPgTGYMvFHXRVeZA5oaBCaKWkA9VfAyg7qZAPsMpUnsJXHLbSZColZA1i0VylTqYXZCSLlHnrEoOZBb2omSPBwbONnLZCaMWa0aYzZCBMwcTpjUeeWsWRnLaWw6kZD'
    
    message = message

    # Initialize the GraphAPI object
    graph = facebook.GraphAPI(access_token)

    tags_list=tags.extract_tags(message)
    follow_msg="Stay up-to-date with the latest in Sports batting! Follow and like our page 'BetEdge AI' now for the most cutting-edge updates and insights!"



    # Upload the image
    photo = graph.put_photo(image=open(photo_path, 'rb'), album_path='me/photos',message=message+"\n\n"+follow_msg+"\n"+tags_list,  published=True)

    # Get the photo ID
    post_id = photo['post_id']
    if(comment is not None or comment is not "" or comment is not "fluttydev"):
           graph.put_object(post_id, "comments", message=comment)



    print(photo)
    return post_id


def post_story_to_facebook(photo_path, message):
    # Replace these with your actual values
    page_id = '61550840662657'
    access_token = 'EAAJni6rVfXABOyG9SDHjZCZAn1dtPDghQtsKFt3iWJ9oVjOKVNw7aHZB39WgUpbRyvH8Ci61ZB8VPgTGYMvFHXRVeZA5oaBCaKWkA9VfAyg7qZAPsMpUnsJXHLbSZColZA1i0VylTqYXZCSLlHnrEoOZBb2omSPBwbONnLZCaMWa0aYzZCBMwcTpjUeeWsWRnLaWw6kZD'
    
    message = message
    
    # Initialize the GraphAPI object
    graph = facebook.GraphAPI(access_token)
    
    # Upload the image
    photo = graph.put_photo(image=open(photo_path, 'rb'),  album_path='me/stories',  published=True)

    
    # Get the photo ID
    photo_id = photo['id']
    

    
    return photo_id






# post_to_facebook("news/'A.I._interest_is_01.jpg","this a comment","this a comment")

# post_story_to_facebook("news/Iowa_DT_suspended_01.jpg", "Check out this awesome story!")
