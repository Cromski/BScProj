from chatGPTprompts import promptChatGPT
import json

behaviors = json.load(open('behaviors.json', 'r'))

promptChatGPT(0.8, behaviors["Behaviors"][3]["act"], behaviors["Behaviors"][3]["keywords"], "iPhone 15")



