import random
import time
from chatGPTprompts import promptChatGPT
from twitterAPI import post_msg_to_twitter
from web_scraper_selenium import get_twitter_trends
from add_data_to_json import add_tweet_obj, edit_tweet_analytics, get_list_of_tweets_older_than_a_day
from web_scrape_analysis import get_analysis_of_tweet
import json

behaviors = json.load(open('behaviors.json', 'r'))
roundnr = 1
temp = 0.8
#post to single behavior
# topic = get_twitter_trends()[0][1] # get the most trending topic
# tweet = promptChatGPT(0.8, behaviors["Behaviors"][behaviorVal]["act"], behaviors["Behaviors"][behaviorVal]["keywords"], topic)
# post_msg_to_twitter(behaviors["Behaviors"][behaviorVal]["act"], tweet)

#post to all behaviors each 1.5 hours
while True:
    print("round: " + str(roundnr))
    topic = get_twitter_trends()[0][1] # get the most trending topic
    print("topic: " + topic)

    #post to all behaviors
    for i in range(4):

        tweets_to_get_updated = get_list_of_tweets_older_than_a_day(behaviors["Behaviors"][i]["act"])
        print(tweets_to_get_updated)

        for tweet_id in tweets_to_get_updated:
            likes,retweets,comments,impressions,engagements,detail_expands,new_followers,profile_visits = get_analysis_of_tweet(behaviors["Behaviors"][i]["act"], tweet_id)
            edit_tweet_analytics(behaviors["Behaviors"][i]["act"], tweet_id, likes, retweets, comments, impressions, engagements, detail_expands, new_followers, profile_visits)
            

        prompt,tweet = promptChatGPT(temp, behaviors["Behaviors"][i]["act"], behaviors["Behaviors"][i]["keywords"], topic)
        tweet_id = post_msg_to_twitter(behaviors["Behaviors"][i]["act"], tweet)
        add_tweet_obj(behaviors["Behaviors"][i]["act"], str(tweet_id), prompt, tweet)
        
    print(f"round {roundnr} done")
    roundnr += 1
    time.sleep(random.randint(3600, 7200))