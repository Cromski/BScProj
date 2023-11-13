import os
import tweepy
import io
import requests
from colorama import Fore, Style
import tempfile
from dotenv import load_dotenv

load_dotenv()

def init_twitter_client(behavior):
    behavior = behavior.upper()
    consumer_key = os.getenv(f"{behavior}_X_API_KEY")
    consumer_secret = os.getenv(f"{behavior}_X_API_KEY_SECRET")
    access_token = os.getenv(f"{behavior}_X_ACCESS_TOKEN")
    access_token_secret = os.getenv(f"{behavior}_X_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api_v1 = tweepy.API(auth)
    api_v2 = tweepy.Client(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret)
    return api_v1,api_v2

def post_to_twitter(api_v1,api_v2, message, behavior, image_url=None):
    
    # Create the tweet with the optional image
    # add image_url to the media_ids keyword argument if you want to attach media to any of the statuses you’re posting.
    response = requests.get(image_url)
    image_content = response.content

    # Save the image content to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(image_content)
        temp_file_path = temp_file.name

    try:
        # Upload the image using api_v2.media.upload
        media = api_v1.media_upload(temp_file_path)
        media_id = media.media_id
        tweet = api_v2.create_tweet(text=message, media_ids=[media_id])
        print(Fore.GREEN + f'\n####---> Posted: Behavior={behavior} ID={tweet[0]["id"]}, QUOTE={message}' + Style.RESET_ALL)
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)
    
    
    return tweet[0]["id"]

def post_msg_to_twitter(behavior, message, image_url=None):
    api_v1,api_v2 = init_twitter_client(behavior)
    return post_to_twitter(api_v1,api_v2,message,behavior, image_url=image_url)
