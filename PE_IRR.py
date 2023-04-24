#this program generates a graph which visually explains the different Private Equity IRRs for certain PE-type funds
#The approach for this visualization is based on data provided by Preqin Pro, approachable at https://www.preqin.com/insights/blogs/what-are-the-average-private-equity-returns-by-fund-type
#all relevant imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as st
import math
import scipy.stats as stats
import networkx as nx

#this is a single list of private equity strategies
private_equity = ['Early Stage','Venture Capital', 'Growth Equity', 'Buyouts',]

#nodes for label below the x axis
label_below_x_axis = ['Early Stage', 'Venture Capital', 'Growth Equity','Buyouts',]

#creates an nx graph
G = nx.DiGraph()

#draws lines as x and y axis
plt.plot([0, 0], [0, 10], linewidth=2, color = 'black')
plt.plot([0, 18], [0, 0], linewidth=2, color = 'black')


#creates nodes for the private equity strategies
G.add_node(private_equity[0], color = 'lightblue', size = 2500)
G.add_node(private_equity[1], color = 'blue', size = 3500)
G.add_node(private_equity[2], color = 'gray', size = 3500)
G.add_node(private_equity[3], color = 'black', size = 5590)

#create nodes for the label below the x axis
G.add_node(label_below_x_axis[0], color = 'lightblue', size = 200)
G.add_node(label_below_x_axis[1], color = 'blue', size = 200)
G.add_node(label_below_x_axis[2], color = 'gray', size = 200)
G.add_node(label_below_x_axis[3], color = 'black', size = 200)

#creates a grid
for i in range(0, 11):
    plt.plot([0, 18], [i, i], linewidth=0.5, color = 'gray',alpha = 1,zorder=0)
for i in range(0, 19):
    plt.plot([i, i], [0, 10], linewidth=0.5, color = 'gray',alpha = 1,zorder=0)


#manual postioning of nodes
pos = {}
pos[private_equity[0]] = (12.65, 8.35)
pos[private_equity[1]] = (8.95, 6.85)
pos[private_equity[2]] = (5.5, 5.75)
pos[private_equity[3]] = (7, 4.74)

pos2 = {}
pos2[label_below_x_axis[0]] = (4, -2)
pos2[label_below_x_axis[1]] = (7.65, -2)
pos2[label_below_x_axis[2]] = (11.2, -2)
pos2[label_below_x_axis[3]] = (13.6, -2)

#sets different sizes of the nodes
sizes = [2000, 2800, 2800, 4472]

#sets different colors of the nodes
colors = ['red', 'blue', 'gray', 'black']

#sets text boxes for percentage of IRR
plt.text(0, -0.5, '11%', fontsize=10)
plt.text(1.85, -0.5, '12%', fontsize=10)
plt.text(3.85, -0.5, '13%', fontsize=10)
plt.text(5.85, -0.5, '14%', fontsize=10)
plt.text(7.85, -0.5, '15%', fontsize=10)
plt.text(9.85, -0.5, '16%', fontsize=10)
plt.text(11.85, -0.5, '17%', fontsize=10)
plt.text(13.85, -0.5, '18%', fontsize=10)
plt.text(15.85, -0.5, '19%', fontsize=10)
plt.text(17.85, -0.5, '20%', fontsize=10)

#sets text boxes for percentage of standard deviation
plt.text(-0.95, 0, '0%', fontsize=10)
plt.text(-0.95, 1.85, '5%', fontsize=10)
plt.text(-0.95, 3.85, '10%', fontsize=10)
plt.text(-0.95, 5.85, '15%', fontsize=10)
plt.text(-0.95, 7.85, '20%', fontsize=10)
plt.text(-0.95, 9.85, '25%', fontsize=10)

#sets the x and y axis labels as text boxes
plt.text(-1.5, 1.75, 'Risk - Standard Deviation of Net IRR', fontsize=10, rotation = 90)
plt.text(7.25, -1.2, 'Return - Median Net IRR', fontsize=10)



#sets labels for PE strategies left to the nodes at the x axis
plt.text(1.6, -2.1, 'Early Stage', fontsize=10)
plt.text(4.6, -2.1, 'Venture Capital', fontsize=10)
plt.text(8.4, -2.1, 'Growth Equity', fontsize=10)
plt.text(11.85, -2.1, 'Buyouts', fontsize=10)


#draws everything
nx.draw(G, pos, node_color = colors, node_size = sizes, with_labels = False)
nx.draw(G, pos2, node_color = colors, node_size = 200, with_labels = False)

#plots
plt.show()






