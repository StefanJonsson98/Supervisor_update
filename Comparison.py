#This program generates a tree diagram of the classes of all alternative investments, and the sub-classes of each class.

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import statistics as st
import math
import scipy.stats as stats

#this is a single list of alternative investments
alternative_investments = ['Alternative Investments']

#this is a list of the biggest seven alternative investment classes
classes = ['Private Equity', 'Private Debt', 'Hedge Funds', 'Real Estate','Infrastructure', 'Commodities', 'Collectibles', 'Structured Products']

#this is a list of the sub-classes of Private Equity
private_equity = ['Venture Capital', 'Growth Equity', 'Buyouts', 'Angel Investing']

#draws alternative investments as a node
G = nx.DiGraph()
G.add_node(alternative_investments[0])

#adds manual positions for the nodes
pos = {}
pos[alternative_investments[0]] = (5, 7)
pos[classes[0]] = (1, 3)
pos[classes[1]] = (2, 3)
pos[classes[2]] = (3, 3)
pos[classes[3]] = (4, 3)
pos[classes[4]] = (5, 3)
pos[classes[5]] = (6, 3)
pos[classes[6]] = (7, 3)
pos[classes[7]] = (8, 3)
pos[private_equity[3]] = (1, 0)
pos[private_equity[0]] = (3, 0)
pos[private_equity[1]] = (5, 0)
pos[private_equity[2]] = (7, 0)



#adds lines between the nodes (90 degree angles)
G.add_edge(alternative_investments[0], classes[0])
G.add_edge(alternative_investments[0], classes[1])
G.add_edge(alternative_investments[0], classes[2])
G.add_edge(alternative_investments[0], classes[3])
G.add_edge(alternative_investments[0], classes[4])
G.add_edge(alternative_investments[0], classes[5])
G.add_edge(alternative_investments[0], classes[6])
G.add_edge(alternative_investments[0], classes[7])
G.add_edge(classes[0], private_equity[3])
G.add_edge(classes[0], private_equity[0])
G.add_edge(classes[0], private_equity[1])
G.add_edge(classes[0], private_equity[2])   


#draws the lines between the nodes
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[0])], width = 2.0, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[1])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[2])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[3])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[4])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[5])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[6])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(alternative_investments[0], classes[7])], width = 0.5, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(classes[0], private_equity[0])], width = 2.0, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(classes[0], private_equity[1])], width = 2.0, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(classes[0], private_equity[2])], width = 2.0, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')
nx.draw_networkx_edges(G, pos, edgelist = [(classes[0], private_equity[3])], width = 2.0, arrowstyle = '->', arrowsize = 20,   connectionstyle = 'arc3, rad = 0', edge_color = 'black')






#adds a horizontal stacked bar chart to the diagram
plt.barh(-2.5, 2.8, color = 'gray', height = 0.5, label = 'Private Equity')
plt.barh(-2.5, 2.8, color = 'lightgray', height = 0.5, left = 2.8, label = 'Venture Capital')
plt.barh(-2.5, 2.8, color = 'gray', height = 0.5, left = 5.6, label = 'Hedge Funds')



#sets different colors for the nodes
color_map = []
for node in G:
    if node in alternative_investments[0]:
        color_map.append('gray')
    elif node in classes:
        color_map.append('lightgray')
    else:
        color_map.append('lightgray')


#sets the node edge color
node_edge_color = []
for node in G:
    if node in alternative_investments[0]:
        node_edge_color.append('black')
    elif node in classes:
        node_edge_color.append('black')
    else:
        node_edge_color.append('black')


#plots the diagram with the nodes, edges and labels
nx.draw(G, pos, node_color = 'white', with_labels = True, node_size = 2000, font_size = 14, font_color = 'black', font_weight = 'bold', arrows = True, edge_color = 'black', width = 1, alpha = 1, connectionstyle = 'arc3, rad = 0')
plt.savefig('Alternative Investments.png', dpi = 300, bbox_inches = 'tight', pad_inches = 0.1, transparent = True, facecolor = 'white' , edgecolor = 'white', orientation = 'landscape', papertype = 'a4', format = 'png')
plt.show()
#plots 
