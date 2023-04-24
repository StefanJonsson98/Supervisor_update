#This program generates a simple graph which visually explains the different Private Equity strategies used in the differnt stages of a company's life cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import math
import scipy.stats as stats
import networkx as nx

#this is a single list of private equity strategies
private_equity = ['--Friends and Family--','Angel Investing', 'Venture Capital', 'Growth Equity', 'Private Equity','Leveraged Buyouts','IPOs']

#this is a list of the different stages of a company's life cycle
stages = ['Start-up stage','Seed Stage', 'Early Stage', 'Growth Stage', 'Mature Stage']




#creages an nx graph
G = nx.DiGraph()

#draws lines as x and y axis
plt.plot([0, 0], [0, 6], linewidth=2, color = 'black')
plt.plot([0, 11], [0, 0], linewidth=2, color = 'black')

#draws arrows on the x and y axis
plt.arrow(0, 6, 0, 0.01, head_width=0.05, head_length=0.1, color = 'gray')
plt.arrow(11, 0, 0.01, 0, head_width=0.1, head_length=0.05, color = 'black')


#adds private equity strategies as nodes 
G.add_node(private_equity[1], weight = 1, color = 'red')
G.add_node(private_equity[2])
G.add_node(private_equity[3])
G.add_node(private_equity[4])
G.add_node(private_equity[5])
G.add_node(private_equity[6])

#adds manual positions for the nodes
pos = {}
pos[private_equity[1]] = (1, 0.5) 
pos[private_equity[2]] = (3.5, 1.25)
pos[private_equity[3]] = (5.5, 2.5)
pos[private_equity[4]] = (7, 4)
pos[private_equity[5]] = (8.75, 5.25)
pos[private_equity[6]] = (10.5, 6)
pos[stages[0]] = (1, 0)
pos[stages[1]] = (2.5, 0)
pos[stages[2]] = (4, 0)
pos[stages[3]] = (5.5, 0)
pos[stages[4]] = (7, 0)

#sets different colors for the nodes
color_map = []
for node in G:
    if node in private_equity[1]:
        color_map.append('gray')
    else:
        color_map.append('white')

#adds a label at manual position
plt.text(9, 0.5, 'Company Life Cycle/Time', fontsize = 15, color = 'black')

plt.text(-1.0, 5.75, 'Revenue', fontsize = 15, color = 'gray', fontweight = 'bold')

#draws nodes
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[1]], node_size = 200, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[2]], node_size = 600, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[3]], node_size = 1000, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[4]], node_size = 1400, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[5]], node_size = 1800, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos, nodelist = [private_equity[6]], node_size = 2200, node_color = 'lightgray')

#sets the company's life cycle stages as text x axis
plt.text(0, -0.5, stages[0], fontsize = 14, color = 'black', fontweight = 'bold')
plt.text(2, -0.5, stages[1], fontsize = 14, color = 'black', fontweight = 'bold')
plt.text(4, -0.5, stages[2], fontsize = 14, color = 'black', fontweight = 'bold')
plt.text(6, -0.5, stages[3], fontsize = 14, color = 'black', fontweight = 'bold')
plt.text(9, -0.5, stages[4], fontsize = 14, color = 'black', fontweight = 'bold')


#sets different colors for the nodes
color_map = []
for node in G:
    if node in private_equity[1]:
        color_map.append('lightgray')
    else:
        color_map.append('white')

nx.draw(G, pos, with_labels = True, font_size = 15, font_color = 'black', node_color = color_map)
plt.show()