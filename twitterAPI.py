import os
import tweepy
from colorama import Fore, Style
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
    api_v2 = tweepy.Client(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret)
    return api_v2

def post_to_twitter(api_v2,message,behavior):
    tweet = api_v2.create_tweet(text=message)
    print(Fore.GREEN + f'\n####---> Posted: Behavior={behavior} ID={tweet[0]["id"]}, QUOTE={message}' + Style.RESET_ALL)
    return tweet[0]["id"]

def post_msg_to_twitter(behavior, message):
    api_v2 = init_twitter_client(behavior)
    return post_to_twitter(api_v2,message,behavior)
