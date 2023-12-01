import json

behaviors = json.load(open('behaviors.json', 'r'))

all_results = {}

def get_overview_of_one_behavior(behavior):

    with open(f'tweets-with-analytics/{behavior}-data.json', 'r') as json_file:
        data = json.load(json_file)

    total_values = {
        "likes": [],
        "retweets": [],
        "comments": [],
        "impressions": [],
        "engagements": [],
        "detail_expands": [],
        "new_followers": [],
        "profile_visits": []
    }

    for item in data:
        if item["checked"] == "true":
            for key in total_values:
                print()
                total_values[key].append(int(item[key].replace(",","")))

    total_values["total_tweets"] = len(data)

    return total_values

def get_overview_of_all_behaviors():
    for i in range(4):
        behavior_name = behaviors["Behaviors"][i]["act"]
        behavior_data = get_overview_of_one_behavior(behavior_name)
        all_results[behavior_name] = behavior_data

    with open('data-overview/data-overview.json', 'w') as output_json:
        json.dump(all_results, output_json, indent=4)
