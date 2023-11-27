from dotenv import load_dotenv
import os
import requests
from datetime import datetime

# """Using strictly less than 200 characters, write something about {topic} in an extremely {act} way, \
#     it should be opinionated. It should not include these words, but have the vibe of them: {keywords}. Write it as a tweet, with minimum 3 hashtags.\
#     Do include any quotation marks, but you may include any emojis.\
#     """

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/chat/completions"

def promptChatGPT(temp, act, keywords, topic, max_retries=3):
    prompt = f"""Using strictly less than 200 characters AND imagine the vibe is are these adjectives: {keywords}, rewrite this in an extremely {act} way, but the most important part is, that your output must be less than 200 characters: {topic}"""
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

    for _ in range(max_retries):
        try:
            response = requests.request("POST", URL, headers=headers, json=payload, stream=False)
            tweet = response.json()['choices'][0]['message']['content']
            return prompt,tweet.replace('"', '')  # Return the result if successful
        except KeyError as e:
            # Handle the KeyError and print an error message
            print(f"KeyError: {e} - Response format is not as expected")


    return prompt,tweet.replace('"', '')



