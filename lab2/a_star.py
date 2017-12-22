from search import *
from graphs import *
import Queue
from lab2 import path_length




def main():
    print "\n Result is: {}\n".format(a_star(NEWGRAPH1, 'S', 'G'))
    # NEWGRAPH1, 'S', 'G'
    # 'SCEG'
    pass

def a_star(graph, start, goal):
    if start == goal:   return [start]
    q = Queue.PriorityQueue() # set up Q as PriorityQueue
    explored_nodes = set() # contain nodes that has been explored, avoiding loop
    q._put( (graph.get_heuristic(start, goal), [start]) ) # put tuple (distance, list of nodes) into Queue

    while q.queue.__len__() != 0:
        u_tuple = q._get()
        u = u_tuple[1][-1] # u_tuple[1] gives the list of nodes, [-1] returns the last node in the list
        explored_nodes.add(u)
        for v in graph.get_connected_nodes(u):
            temp_l = u_tuple[1][:] # assign the list in tuple (distance, list of nodes) to temp_l such that very adjacent node would have the original list in u_tuple
            temp_dist = u_tuple[0]
            if v not in explored_nodes:
                temp_l.append(v) # create a new path with node v as the last node
                temp_dist += path_length(graph, [u, v]) # get a distance of the u_tuple---v path
                q._put( (temp_dist + graph.get_heuristic(v, goal), temp_l) )
                if v == goal:
                    return temp_l

if __name__ == "__main__":
    main()