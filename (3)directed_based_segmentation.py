import pandas as pd

df = pd.read_csv('(2)time_window_filtered.csv') 

# Clean Dir column
df['Dir'] = df['Dir'].str.strip()

# Separate based on flow direction
df_outgoing = df[df['Dir'] == '->']
df_incoming = df[df['Dir'] == '<->']

# Display count of each
print("Outgoing flows (->):", len(df_outgoing))
print("Incoming flows (<->):", len(df_incoming))

# Save to separate CSVs
df_outgoing.to_csv('(3)outgoing_directed.csv', index=False)
df_incoming.to_csv('(3)incoming_directed.csv', index=False)


