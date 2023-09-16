import requests
import os
from dotenv import load_dotenv
from twitter import *

load_dotenv()

con_x_api_key = os.getenv("CONTROVERSIAL_X_API_KEY") # token
con_x_api_key_secret = os.getenv("CONTROVERSIAL_X_API_KEY_SECRET") # token secret
con_x_access_key = os.getenv("CONTROVERSIAL_X_ACCESS_TOKEN") # consumer key
con_x_access_key_secret = os.getenv("CONTROVERSIAL_X_ACCESS_TOKEN_SECRET") # consumer secret
con_x_bearer_token = os.getenv("CONTROVERSIAL_X_BEARER_TOKEN") # consumer secret

t = Twitter(auth=OAuth(con_x_access_key, con_x_access_key_secret, con_x_api_key, con_x_api_key_secret))

t.post.statuses.update(status="Testing 1 2 3")


# URL = "https://api.twitter.com/1.1/statuses/update.json?status=hello"

# headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {con_x_bearer_token}",
#     }

# payload = {
#     "text": "Testing 1 2 3"
# }

# response = requests.request("POST", URL, headers=headers)

# print(response.json())