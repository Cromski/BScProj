import seaborn as sns
import matplotlib.pyplot as plt
import json
import pandas as pd

with open('data-overview/data-overview.json', 'r') as json_file:
    original_data = json.load(json_file)

all_attributes = ['likes', 'retweets', 'comments', 'impressions', 'engagements', 'detail_expands', 'new_followers', 'profile_visits']

def create_boxplot(attribute):

    data = {}

    for behavior, attributes_data in original_data.items():
        if behavior not in data:
            data[behavior] = {}

        if attribute in attributes_data:
            data[behavior][attribute] = attributes_data[attribute]

    # Create a DataFrame from the data
    behavior_data = pd.DataFrame([(behavior, attr) for behavior, data in data.items() for attr in data[attribute]], columns=['Behavior', attribute.capitalize()])

    # Create a boxplot using Seaborn
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")  # Set the style

    # Specify the desired y-axis ticks
    y_ticks = [i for i in range(0, max(behavior_data[attribute.capitalize()]) + 1, 5)]

    sns.boxplot(x="Behavior", y=attribute.capitalize(), data=behavior_data, palette="Set3", hue="Behavior")
    plt.title(f"Boxplot of {attribute.capitalize()} by Behavior")
    plt.xlabel("Behavior")
    plt.ylabel(attribute.capitalize())

    # Set the y-axis ticks
    plt.yticks(y_ticks)

    plt.savefig(f'data-overview/{attribute}-boxplot.png')


def create_all_boxplots():
    for attr in all_attributes:
        create_boxplot(attr)
