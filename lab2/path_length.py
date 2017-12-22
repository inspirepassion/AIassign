from graphs import *
from search import *


# NEWGRAPH2, list('HDCECSBSA')
def path_length(graph, node_names):
    distance = 0
    if node_names.__len__() ==0 : return distance
    for i in range(node_names.__len__()-1):
        distance += graph.get_edge(node_names[i],node_names[i+1]).length
    return distance

print path_length(NEWGRAPH2, list('HDCECSBSA'))