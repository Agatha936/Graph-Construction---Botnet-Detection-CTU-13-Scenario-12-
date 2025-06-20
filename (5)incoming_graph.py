import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('(3)incoming_directed.csv')

# Botnet IPs
bot_ips = ['147.32.84.165', '147.32.84.191', '147.32.84.192']

# Build Graph: incoming flow (victim -> bot)
G = nx.DiGraph()

for _, row in df.iterrows():
    src = row['DstAddr']  
    dst = row['SrcAddr']  
    weight = row['TotBytes']
    
    if G.has_edge(src, dst):
        G[src][dst]['weight'] += weight
    else:
        G.add_edge(src, dst, weight=weight)

G.remove_edges_from(nx.selfloop_edges(G))

# Layout positioning
all_nodes = list(G.nodes())
non_bot_nodes = [n for n in all_nodes if n not in bot_ips]

circle_pos = nx.circular_layout(non_bot_nodes)

bot_pos = {}
bot_radius = 0.2
angle_step = 2 * np.pi / len(bot_ips)
for i, bot in enumerate(bot_ips):
    angle = i * angle_step
    x = bot_radius * np.cos(angle)
    y = bot_radius * np.sin(angle)
    bot_pos[bot] = np.array([x, y])

pos = {**circle_pos, **bot_pos}

# Node color 
node_colors = ['red' if node in bot_ips else 'skyblue' for node in G.nodes()]

# Plotting
plt.figure(figsize=(16, 12))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=1000, node_color=node_colors)

# Draw edges 
nx.draw_networkx_edges(
    G, pos,
    edge_color='black',
    width=1,
    arrows=True,
    arrowstyle='-|>',
    arrowsize=15,
    connectionstyle='arc3,rad=0.08'
)

# Draw IP labels
nx.draw_networkx_labels(G, pos, font_size=9)

# Edge labels (TotBytes)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=edge_labels,
    font_size=8,
    font_color='red',
    label_pos=0.2,           # tengah edge
)

# Display bot IP list in corner
bot_text = '\n'.join(["Botnet IP Address:"] + bot_ips)
plt.text(
    x=1.05, y=1.0, s=bot_text,
    fontsize=11, bbox=dict(facecolor='white', edgecolor='black'),
    transform=plt.gca().transAxes
)

plt.title("                                                      ", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.savefig("(5)incoming.png", dpi=300, bbox_inches='tight')
plt.show()
