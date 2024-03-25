import pandas as pd

def merge_user_data(*args):
    combined_data = pd.DataFrame()
    
    for file in args:
        data = pd.read_csv(file)
        
        if 'Имя' in data.columns:
            data.rename(columns={'Имя': 'First Name'}, inplace=True)
        
        if 'Местоположение' in data.columns:
            data.rename(columns={'Местоположение': 'Location'}, inplace=True)
            
        combined_data = pd.concat([combined_data, data], ignore_index=True)
    
    return combined_data

merged_data = merge_user_data('users_1.csv', 'users_2.csv')
print(merged_data)

merged_data.to_csv('combined_user_data.csv', index=False)
