from chatGPTprompts import promptChatGPT
from twitterAPI import post_msg_to_twitter
import json

behaviors = json.load(open('behaviors.json', 'r'))

#post to single behavior
# behaviorVal = 0
# tweet = promptChatGPT(0.8, behaviors["Behaviors"][behaviorVal]["act"], behaviors["Behaviors"][behaviorVal]["keywords"], "#IDontWantToOverreactBUT")
# post_msg_to_twitter(behaviors["Behaviors"][behaviorVal]["act"], tweet)

#post to all behaviors
for i in range(4):
    tweet = promptChatGPT(0.8, behaviors["Behaviors"][i]["act"], behaviors["Behaviors"][i]["keywords"], "Nintendo")
    post_msg_to_twitter(behaviors["Behaviors"][i]["act"], tweet)