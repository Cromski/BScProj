from chatGPTprompts import promptChatGPT
from twitterAPI import post_msg_to_twitter
from web_scraper_selenium import get_twitter_trends
import json

behaviors = json.load(open('behaviors.json', 'r'))

temp = 0.8
topic = get_twitter_trends()[0][1] # get the most trending topic
#post to single behavior
# behaviorVal = 0
# tweet = promptChatGPT(0.8, behaviors["Behaviors"][behaviorVal]["act"], behaviors["Behaviors"][behaviorVal]["keywords"], "#IDontWantToOverreactBUT")
# post_msg_to_twitter(behaviors["Behaviors"][behaviorVal]["act"], tweet)

#post to all behaviors
for i in range(4):
    tweet = promptChatGPT(temp, behaviors["Behaviors"][i]["act"], behaviors["Behaviors"][i]["keywords"], topic)
    post_msg_to_twitter(behaviors["Behaviors"][i]["act"], tweet)