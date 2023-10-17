from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/chat/completions"

def promptChatGPT(temp, act, keywords, topic):
    prompt = f"""Using strictly less than 200 characters, write something about {topic} in an extremely {act} way, \
    it should be opinionated. It should not include these words, but have the vibe of them: {keywords}. Write it as a tweet, with minimum 3 hashtags.\
    Do include any quotation marks, but you may include any emojis.\
    """
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temp, # temperature high = more creative
        "top_p": 1,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 0,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    response = requests.request("POST", URL, headers=headers, json=payload, stream=False)
    try:
        tweet = response.json()['choices'][0]['message']['content']
    except KeyError as e:
            print(f"KeyError: {e} - Response format is not as expected")

    if tweet.__contains__('"'): # remove quotes if present, not possible to prompt it out...
        tweet = tweet.replace('"', '')

    return prompt,tweet



