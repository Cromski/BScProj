from chatGPTprompts import promptChatGPT
import json

behaviors = json.load(open('behaviors.json', 'r'))

promptChatGPT(0.8, behaviors["Behaviors"][0]["act"], behaviors["Behaviors"][0]["keywords"], "iPhone 15")
