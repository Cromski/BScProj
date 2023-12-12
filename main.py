import random
import time
from datetime import datetime
from chatGPTprompts import promptChatGPT
from twitterAPI import post_msg_to_twitter
# from web_scraper_selenium import get_twitter_trends
from fetch_popular_tweet_by_trend_scraper import get_twitter_trends
from add_data_to_json import add_tweet_obj, edit_tweet_analytics, get_list_of_tweets_older_than_a_day
from web_scrape_analysis import get_analysis_of_tweet
from get_overview_of_all_data import get_overview_of_all_behaviors
from create_boxplots import create_all_boxplots
from colorama import Fore, Style
import json

behaviors = json.load(open('behaviors.json', 'r'))
roundnr = 1
temp = 0.8

while True:
    print(Fore.MAGENTA + f"########## Round {str(roundnr)} started @ {datetime.now().strftime('%H:%M:%S')} ##########" + Style.RESET_ALL)

    print(Fore.CYAN + f'####---> Updating data from tweets if any')
    # Update all tweet analytics
    for i in range(4):
        tweets_to_get_updated = get_list_of_tweets_older_than_a_day(behaviors["Behaviors"][i]["act"])

        for tweet_id in tweets_to_get_updated:
            likes,retweets,comments,impressions,engagements,detail_expands,new_followers,profile_visits = get_analysis_of_tweet(behaviors["Behaviors"][i]["act"], tweet_id)
            edit_tweet_analytics(behaviors["Behaviors"][i]["act"], tweet_id, likes, retweets, comments, impressions, engagements, detail_expands, new_followers, profile_visits)
        
        if len(tweets_to_get_updated) > 0: print(Fore.CYAN + f'\n####---> Data updated from tweets ({behaviors["Behaviors"][i]["act"]}): ' + str(tweets_to_get_updated) + Style.RESET_ALL)

    print(Fore.CYAN + f'\n####---> All tweets posted' + Style.RESET_ALL)

    get_overview_of_all_behaviors()
    create_all_boxplots()

    popular_tweet,popular_tweet_src = get_twitter_trends() # get the most trending topic

    print(Fore.CYAN + f'\n####---> Topic chosen: {popular_tweet}' + Style.RESET_ALL)
    # post to all behaviors
    for i in range(4):
        prompt,tweet = promptChatGPT(temp, behaviors["Behaviors"][i]["act"], behaviors["Behaviors"][i]["keywords"], popular_tweet)
        tweet_id = post_msg_to_twitter(behaviors["Behaviors"][i]["act"], tweet,popular_tweet_src)
        add_tweet_obj(behaviors["Behaviors"][i]["act"], str(tweet_id), prompt, tweet, popular_tweet_src)
        

    print(Fore.CYAN + f'\n####---> All boxplots created' + Style.RESET_ALL)

    print(Fore.BLUE + f"##### round {roundnr} done @ {datetime.now().strftime('%H:%M:%S')} #####\n" + Style.RESET_ALL)
    roundnr += 1
    time.sleep(random.randint(3600, 7200))