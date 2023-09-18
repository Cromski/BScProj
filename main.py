from chatGPTprompts import promptChatGPT
from twitterAPI import post_msg_to_twitter
import json

behaviors = json.load(open('behaviors.json', 'r'))

tweet = promptChatGPT(0.8, behaviors["Behaviors"][3]["act"], behaviors["Behaviors"][3]["keywords"], "iPhone 15")
post_msg_to_twitter(tweet)