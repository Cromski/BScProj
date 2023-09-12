from chatGPTprompts import promptChatGPT
import json

behaviors = json.load(open('behaviors.json', 'r'))

promptChatGPT(0.3, behaviors["Behaviors"][1]["act"], behaviors["Behaviors"][1]["keywords"], "iPhone 15")



