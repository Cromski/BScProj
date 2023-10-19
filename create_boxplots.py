import seaborn as sns
import matplotlib.pyplot as plt
import json
import pandas as pd

def create_boxplot(attribute, data_overview, show_outliers=True):

    data = {}

    for behavior, attributes_data in data_overview.items():
        if behavior not in data:
            data[behavior] = {}

        if attribute in attributes_data:
            data[behavior][attribute] = attributes_data[attribute]

    # Create a DataFrame from the data
    behavior_data = pd.DataFrame([(behavior, attr) for behavior, data in data.items() for attr in data[attribute]], columns=['Behavior', attribute.capitalize()])

    # Create a boxplot using Seaborn
    plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
    sns.set(style="whitegrid")  # Set the style

    if show_outliers:
        # y_ticks = [i for i in range(0, max(behavior_data[attribute.capitalize()]) + 1, 5)]
        sns.boxplot(x="Behavior", 
                    y=attribute.capitalize(), 
                    data=behavior_data, 
                    palette="Set3", 
                    hue="Behavior", 
                    showfliers=True, 
                    showmeans=True,
                    meanprops={"marker": "+",
                       "markeredgecolor": "green",
                       "markersize": "10"})
    else:
        sns.boxplot(x="Behavior", 
                    y=attribute.capitalize(), 
                    data=behavior_data, 
                    palette="Set3", 
                    hue="Behavior", 
                    showfliers=False, 
                    showmeans=True,
                    meanprops={"marker": "+",
                       "markeredgecolor": "green",
                       "markersize": "10"})
    plt.title(f"Boxplot of {attribute.capitalize()} by Behavior")
    plt.xlabel("Behavior")
    plt.ylabel(attribute.capitalize())

    if show_outliers:
        # plt.yticks(y_ticks)
        plt.savefig(f'data-overview/{attribute}-boxplot.png')
    else:
        plt.savefig(f'data-overview/{attribute}-boxplot-without-outliers.png')
        create_boxplot(attribute, data_overview, show_outliers=True)
    plt.close('all')

def create_all_boxplots():
    with open('data-overview/data-overview.json', 'r') as json_file:
        data_overview = json.load(json_file)

    all_attributes = ['likes', 'retweets', 'comments', 'impressions', 'engagements', 'detail_expands', 'new_followers', 'profile_visits']
    
    for attr in all_attributes:
        if attr == "impressions":
            create_boxplot(attr, data_overview, show_outliers=False)
        else:
            create_boxplot(attr, data_overview)

create_all_boxplots()
