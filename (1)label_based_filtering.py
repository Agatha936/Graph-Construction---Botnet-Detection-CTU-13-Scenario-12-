import pandas as pd

df = pd.read_csv('capture20110819.binetflow')  

# Filter rows (where 'Label' contains 'Botnet') 
botnet_df = df[df['Label'].str.contains('botnet', case=False, na=False)]

# Display records
print(botnet_df.head())

# Save to a new CSV file
botnet_df.to_csv('(1)label_based_filtering.csv', index=False)
