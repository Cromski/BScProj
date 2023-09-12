from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/chat/completions"

def promptChatGPT(temp, act, keywords, topic):
    prompt = f"""In strictly less than 200 characters, write something about {topic} in an extremely {act} way, \
    it should be opinionated. It should not include these words, but have the vibe of them: {keywords}. Write it as a tweet.\
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

    print(response.json())

    with open(f'./ChatGPT-prompt-output/{act}.txt', 'a') as f:
        f.write(
            f"date: {datetime.now().strftime('%d/%m-%Y, %H:%M:%S') }\nprompt: {prompt}\nresponse: {response.json()['choices'][0]['message']['content']}\n\n")



