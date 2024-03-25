import os
import pandas as pd

if not os.path.exists('data'):
    os.makedirs('data')

def analyze_user_data(directory):
    user_data = []

    for file in os.listdir(directory):
        if file.endswith(".csv"):
            file_path = os.path.join(directory, file)
            df = pd.read_csv(file_path)
            user_data.append(df)

    combined_data = pd.concat(user_data, ignore_index=True)

    return combined_data

def display_summary(data):
    print("Summary of user data:")
    print(data.describe())

def filter_data(data, column, value):
    filtered_data = data[data[column] == value]
    return filtered_data

directory = "data" 
all_user_data = analyze_user_data(directory)
display_summary(all_user_data)

filtered_data = filter_data(all_user_data, 'age', 30)
print("\nFiltered data (age 30):")
print(filtered_data)

filtered_data = filter_data(all_user_data, 'location', 'New York')
print("\nFiltered data (location New York):")
print(filtered_data)
