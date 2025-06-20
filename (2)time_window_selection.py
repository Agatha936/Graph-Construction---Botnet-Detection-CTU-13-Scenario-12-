import pandas as pd

df = pd.read_csv('(1)label_based_filtering.csv')

# Convert 'StartTime' to datetime 
df['StartTime'] = pd.to_datetime(df['StartTime'])

# Filter rows 
start_time = pd.to_datetime('2011/08/19 10:53:00')
end_time = pd.to_datetime('2011/08/19 11:05:00')
df_filtered_time = df[(df['StartTime'] >= start_time) & (df['StartTime'] <= end_time)]

# Display rows
print(df_filtered_time.head())

# Save the filtered data
df_filtered_time.to_csv('(2)time_window_filtered.csv', index=False)


