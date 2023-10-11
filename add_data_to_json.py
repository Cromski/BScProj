import json
import datetime
import time

def add_tweet_obj(behavior, id, prompt, tweet):
    try:
        with open(f'tweets-with-analytics/{behavior}-data.json', 'r') as file:
            existing_data = json.load(file)
    except:
        existing_data = []

    date = datetime.datetime.now()
    unix_timestamp = time.mktime(date.timetuple())

    new_data = {
        "id": id,
        "date": str(date),
        "unix_timestamp": unix_timestamp,
        "checked": "false",
        "prompt": prompt,
        "tweet": tweet,
        "likes": "0",
        "retweets": "0",
        "comments": "0",
        "impressions": "0",
        "engagements": "0",
        "detail_expands": "0",
        "new_followers": "0",
        "profile_visits": "0"
    }

    existing_data.insert(0, new_data)

    with open(f'tweets-with-analytics/{behavior}-data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

def get_list_of_tweets_older_than_a_day(behavior):
    try:
        with open(f'tweets-with-analytics/{behavior}-data.json', 'r') as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        existing_data = []

    tweets_older_than_a_day = []


    for data_object in existing_data:
        if data_object["checked"] == "false" and float(data_object["unix_timestamp"]) < time.time() - 86400:
            tweets_older_than_a_day.append(data_object["id"])

    return tweets_older_than_a_day

def edit_tweet_analytics(behavior, id, likes, retweets, comments, impressions, engagements, detail_expands, new_followers, profile_visits):
    
    with open(f'tweets-with-analytics/{behavior}-data.json', 'r') as file:
        existing_data = json.load(file)

    target_id = id

    for data_object in existing_data:
        if data_object["id"] == target_id:
            data_object["checked"] = "true"
            data_object["likes"] = likes
            data_object["retweets"] = retweets
            data_object["comments"] = comments
            data_object["impressions"] = impressions
            data_object["engagements"] = engagements
            data_object["detail_expands"] = detail_expands
            data_object["new_followers"] = new_followers
            data_object["profile_visits"] = profile_visits

    with open(f'tweets-with-analytics/{behavior}-data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)



# debug:
# add_tweet_obj("sad", "123444", "prompt", "tweet")

# print(get_list_of_tweets_older_than_a_day("sad"))

# edit_tweet_analytics("sad", "123444", "1", "2", "3", "4", "5", "6", "7", "8")