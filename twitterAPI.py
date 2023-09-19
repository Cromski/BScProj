import os
import tweepy
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()


# credits for twitter authorization: https://github.com/loonathedorm/Twitter-Tracery-Bot/tree/main
def init_twitter_client(behavior):
    """Initialising Twitter API Client"""
    # Getting Twitter API Keys
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
    return api_v1, api_v2

def post_to_twitter(api_v2,message):
    tweet = api_v2.create_tweet(text=message)
    print(Fore.GREEN + f'\n####---> Posted: ID={tweet[0]["id"]}, QUOTE={message}' + Style.RESET_ALL)

def post_msg_to_twitter(behavior, message):
    api_v2 = init_twitter_client(behavior)[1]
    post_to_twitter(api_v2,message)
