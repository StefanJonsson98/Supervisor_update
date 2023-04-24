#This program generates a simple xy graph which visually explains the different Private Equity strategies used in the differnt stages of a company's life cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import scipy.stats as stats
import networkx as nx

#this is a single list of private equity strategies
private_equity = ['--Friends and Family--','Angel Investing', 'Venture Capital', 'Growth Equity', 'Private Equity','Buyouts','IPOs']

#this is a list of the different stages of a company's life cycle
stages = ['Start-up stage','Seed Stage', 'Early Stage', 'Growth Stage', 'Mature Stage']

#nodes for risk involved (6 nodes)
risk_involved = ['--Friends and Family--','Angel Investing', 'Venture Capital', 'Growth Equity', 'Private Equity','Buyouts','IPOs']


#nodes for the investment size (6 nodes)
investment_size = ['--Friends and Family--','Angel Investing', 'Venture Capital', 'Growth Equity', 'Private Equity','Buyouts','IPOs']


#creages an nx graph
G = nx.DiGraph()

#draws lines as x and y axis
plt.plot([0, 0], [0, 6], linewidth=2, color = 'black')
plt.plot([0, 11], [0, 0], linewidth=2, color = 'black')

#draws arrows on the x and y axis
plt.arrow(0, 6, 0, 0.01, head_width=0.05, head_length=0.1, color = 'gray')
plt.arrow(11, 0, 0.01, 0, head_width=0.1, head_length=0.05, color = 'black')


#adds private equity strategies as nodes 
G.add_node(private_equity[1])
G.add_node(private_equity[2])
G.add_node(private_equity[3])
G.add_node(private_equity[4])
G.add_node(private_equity[5])
G.add_node(private_equity[6])

#adds risk involved as nodes
G.add_node(risk_involved[1])
G.add_node(risk_involved[2])
G.add_node(risk_involved[3])
G.add_node(risk_involved[4])
G.add_node(risk_involved[5])
G.add_node(risk_involved[6])

#adds investment size as nodes
G.add_node(investment_size[1])
G.add_node(investment_size[2])
G.add_node(investment_size[3])
G.add_node(investment_size[4])
G.add_node(investment_size[5])
G.add_node(investment_size[6])



#adds manual positions for the nodes
pos1 = {}
pos1[private_equity[1]] = (1, 0.5) 
pos1[private_equity[2]] = (3.5, 1.25)
pos1[private_equity[3]] = (5.5, 2.5)
pos1[private_equity[4]] = (7.5, 4)
pos1[private_equity[5]] = (9.25, 5)
pos1[private_equity[6]] = (11, 5.5)
pos1[stages[0]] = (1, 0)
pos1[stages[1]] = (2.5, 0)
pos1[stages[2]] = (4, 0)
pos1[stages[3]] = (5.5, 0)
pos1[stages[4]] = (7, 0)

pos2 = {}
pos2[risk_involved[1]] = (0.0, 5.5)
pos2[risk_involved[2]] = (2.5, 5.25)
pos2[risk_involved[3]] = (4.5, 4.5)
pos2[risk_involved[4]] = (6.5, 3.5)
pos2[risk_involved[5]] = (8.5, 2.0)
pos2[risk_involved[6]] = (10.5, 1)

pos3 = {}
pos3[investment_size[1]] = (0.0, 0.75)
pos3[investment_size[2]] = (3.5, 2.25)
pos3[investment_size[3]] = (5.5, 3.5)
pos3[investment_size[4]] = (7.5, 5)
pos3[investment_size[5]] = (9.5, 6.25)
pos3[investment_size[6]] = (10.5, 6.5)


#sets different colors for the nodes
color_map = []
for node in G:
    if node in private_equity[1]:
        color_map.append('gray')
    else:
        color_map.append('white')

#sets different colors for the labels
label_color_map = []
for node in G:
    if node in private_equity[1]:
        label_color_map.append('black')
    else:
        label_color_map.append('white')

#adds a label at manual position
plt.text(6.5, 0.5, 'Company Life Cycle/Time', fontsize = 15, color = 'black')

plt.text(-0.1, 6.5, 'Revenue', fontsize = 15, color = 'gray', fontweight = 'bold')

#adds a label at manual position
plt.text(10.5, 0.95, 'Risk Involved', fontsize = 15, color = 'red')

#adds a label at manual position
plt.text(10.5, 6.45, 'Investment Size', fontsize = 15, color = 'blue')

#draws nodes
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[1]], node_size = 200, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[2]], node_size = 600, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[3]], node_size = 1000, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[4]], node_size = 1400, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[5]], node_size = 1800, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos1, nodelist = [private_equity[6]], node_size = 2200, node_color = 'lightgray')

#draws risk involved nodes
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[1]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[2]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[3]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[4]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[5]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos2, nodelist = [risk_involved[6]], node_size = 2, node_color = 'lightgray')

#draws investment size nodes
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[1]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[2]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[3]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[4]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[5]], node_size = 2, node_color = 'lightgray')
nx.draw_networkx_nodes(G, pos3, nodelist = [investment_size[6]], node_size = 2, node_color = 'lightgray')

#draws edges for risk involved nodes
nx.draw_networkx_edges(G, pos2, edgelist = [(risk_involved[1], risk_involved[2])], width = 1, edge_color = 'red', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = -0.1')
nx.draw_networkx_edges(G, pos2, edgelist = [(risk_involved[2], risk_involved[3])], width = 1, edge_color = 'red', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.0')
nx.draw_networkx_edges(G, pos2, edgelist = [(risk_involved[3], risk_involved[4])], width = 1, edge_color = 'red', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.0')
nx.draw_networkx_edges(G, pos2, edgelist = [(risk_involved[4], risk_involved[5])], width = 1, edge_color = 'red', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = -0.02')
nx.draw_networkx_edges(G, pos2, edgelist = [(risk_involved[5], risk_involved[6])], width = 1, edge_color = 'red', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.1')

#draws edges for investment size nodes
nx.draw_networkx_edges(G, pos3, edgelist = [(investment_size[1], investment_size[2])], width = 1, edge_color = 'blue', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.1')
nx.draw_networkx_edges(G, pos3, edgelist = [(investment_size[2], investment_size[3])], width = 1, edge_color = 'blue', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.0')
nx.draw_networkx_edges(G, pos3, edgelist = [(investment_size[3], investment_size[4])], width = 1, edge_color = 'blue', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = 0.0')
nx.draw_networkx_edges(G, pos3, edgelist = [(investment_size[4], investment_size[5])], width = 1, edge_color = 'blue', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = -0.02')
nx.draw_networkx_edges(G, pos3, edgelist = [(investment_size[5], investment_size[6])], width = 1, edge_color = 'blue', alpha = 1, style = 'dashed', arrows = True, arrowstyle = '->', arrowsize = 20, connectionstyle = 'arc3, rad = -0.1')


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

#sets colors for all risk involved nodes
color_map2 = []
for node in G:
    if node in risk_involved:
        color_map2.append('white')
    else:
        color_map2.append('white')

nx.draw(G, pos1, with_labels = True, font_size = 15, font_color = 'black', node_color = color_map, node_size = 200, node_shape = 'o', width = 2, edge_color = 'black', arrows = True, arrowstyle = '-|>', arrowsize = 20, connectionstyle = 'arc3, rad = 0.1')
nx.draw(G, pos2, with_labels = False, font_size = 15, font_color = 'black', node_color = color_map2, node_size = 25, node_shape = 'o', width = 2, edge_color = 'black', arrows = False, arrowstyle = '--', arrowsize = 2, connectionstyle = 'arc3, rad = 0.1')
nx.draw(G, pos2, with_labels = False, font_size = 15, font_color = 'black', node_color = color_map2, node_size = 25, node_shape = 'o', width = 2, edge_color = 'black', arrows = False, arrowstyle = '--', arrowsize = 2, connectionstyle = 'arc3, rad = 0.1')
plt.show()