# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.
import Queue
def bfs(graph, start, goal):
    if start == goal: return [start]
    dict_nodes = {}
    for node in graph.nodes:
        dict_nodes[node] = [0, None]

    result = []
    q = Queue.Queue()

    dict_nodes[start] = [1, None]
    q.put(start)
    while q.queue.__len__() != 0:
        u = q.get()
        for v in graph.get_connected_nodes(u):
            if dict_nodes[v][0] == 0:
                dict_nodes[v][0] = 1
                if v is not start:
                    dict_nodes[v][1] = u
                # if v == goal:
                #     break
                # else:
                #     q.put(v)
                q.put(v)
        # if dict_nodes[goal][1] != None:
        #     break
    if dict_nodes[goal][1] == None:
        return result

    else:
        link = dict_nodes[goal][1]
        result.append(goal)
        # print "goal is: {}".format(goal)
        # print "goal's link is: {}\n".format(dict_nodes[goal][1])
        # print "{}'s link is: {}\n".format(dict_nodes[goal][1], dict_nodes[dict_nodes[goal][1]][1])
        # print "{}'s link is: {}\n".format(dict_nodes[dict_nodes[goal][1]][1], dict_nodes[dict_nodes[dict_nodes[goal][1]][1]][1])
        # print "S's link is: {}".format(dict_nodes['S'][1])
        # print "start is: {}".format(start)
        # print "start = S: {}".format(start=='S')
        # print "Stairs' p_link is: {}\n".format(dict_nodes['Stairs'][1])
        # print "Grand Hall's p_link is: {}".format(dict_nodes['Grand Hall'][1])

        while link is not start:
            # print "While Loop: link is: {}".format(link)
            result.insert(0, link)
            link = dict_nodes[link][1]
        result.insert(0, start)

        # return type(result)
        return ''.join(result)
    raise NotImplementedError

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    if start == goal: return [start]
    dict_nodes = {}
    for node in graph.nodes:
        dict_nodes[node] = [0, None]

    result = []
    stack = []

    dict_nodes[start] = [1,None]
    stack.append(start)
    while stack.__len__() != 0:
        u = stack.pop()
        for v in graph.get_connected_nodes(u):
            if dict_nodes[v][0] == 0:
                dict_nodes[v][0]=1
                if v is not start:
                    dict_nodes[v][1] = u
                # if v == goal:
                #     break
                # else:
                #     q.put(v)
                stack.append(v)
        # if dict_nodes[goal][1] != None:
        #     break
    if dict_nodes[goal][1] == None:
        return result

    else:
        link = dict_nodes[goal][1]
        result.append(goal)
        # print "goal is: {}".format(goal)
        # print "goal's link is: {}\n".format(dict_nodes[goal][1])
        # print "{}'s link is: {}\n".format(dict_nodes[goal][1], dict_nodes[dict_nodes[goal][1]][1])
        # print "{}'s link is: {}\n".format(dict_nodes[dict_nodes[goal][1]][1], dict_nodes[dict_nodes[dict_nodes[goal][1]][1]][1])
        # print "S's link is: {}".format(dict_nodes['S'][1])
        # print "start is: {}".format(start)
        # print "start = S: {}".format(start=='S')
        # print "Stairs' p_link is: {}\n".format(dict_nodes['Stairs'][1])
        # print "Grand Hall's p_link is: {}".format(dict_nodes['Grand Hall'][1])

        while link is not start:
            # print "While Loop: link is: {}".format(link)
            result.insert(0, link)
            link = dict_nodes[link][1]
        result.insert(0, start)

        # return type(result)
        return ''.join(result)
    raise NotImplementedError


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
from collections import *
def hill_climbing(graph, start, goal):
    if start == goal: return [start]
    dict_nodes = {}
    for node in graph.nodes:
        dict_nodes[node] = [0, None]

    result = []
    stack = []
    heuristic_List = []

    dict_nodes[start] = [1,None]
    stack.append(start)
    while stack.__len__() != 0:
        u = stack.pop()
        dict_nodes[u][0] = 2  # mark as black, the node is chosen to be explored
        heuristic_List = []
        for v in graph.get_connected_nodes(u):

            # if dict_nodes[v][0] == 0:
            if dict_nodes[v][0] != 2 and v is not start:
                dict_nodes[v][0]=1
                if v is not start:
                    dict_nodes[v][1] = u
                if v == goal:
                    break
                else:
                    heuristic_List.append(v) # put children into temperary list for sorting heuristic info
                # stack.append(v)
        # sorting elements in heuristic list:
        d = {i:graph.get_heuristic(i,goal) for i in heuristic_List}
        ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for i in ordered_d.items():
            stack = stack+[i[0]]

    if dict_nodes[goal][1] is None:
        return result

    else:
        link = dict_nodes[goal][1]
        result.append(goal)

        while link is not start:
            result.insert(0, link)
            link = dict_nodes[link][1]
        result.insert(0, start)

        # return type(result)
        # return ''.join(result)
        return result
    raise NotImplementedError

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
