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
    if start == goal: return [start]

    q = Queue.Queue()
    explored_nodes = set()

    q.put([start]) # Enqueue each elements in Queue as a list of nodes
    explored_nodes.add(start)
    qLen = q.queue.__len__()
    while qLen != 0:


        loop_num = beam_width
        # print "\nloop_num is {}".format(loop_num)
        # print "Queue is: {}".format(q.queue)
        # print "q.queue.__len__(): {}".format(q.queue.__len__())

        if qLen < beam_width:
            loop_num = qLen

        temp_l = []
        for i in range(loop_num):
            # print "\nloop_num is {}".format(loop_num)
            u = q.get() # As each element in Queue is a list of nodes, this gets the list, Note that the last node in the list q.get()[-1]


            # print "\nu is {}\nAdjacents is {}".format(u[-1], graph.get_connected_nodes(u[-1]))
            # print "num_children is {}".format(graph.get_connected_nodes(u[-1]).__len__())
            # print "Before for loop, the explored_nodes: {}".format(explored_nodes)
            for v in graph.get_connected_nodes(u[-1]):
                if v not in explored_nodes:

                    # print "u is {}".format(u)
                    # print "in this loop, v is {}".format(v)
                    temp = u[:] # assign value of u to temp
                    temp.append(v)
                    temp_l.append((graph.get_heuristic(v,goal), temp))
                    # print "temp_l is {}".format(temp_l)
            # print "After for loop, the explored_nodes: {}".format(explored_nodes)
        # Sort elements in temperary dictionary, such that we could choose the best beam_width elements into Queue
        # ordered_d = OrderedDict(sorted(temp_d.items(), key = lambda x: x[0]))
        temp_l.sort(key=lambda x: x[0])
        # print "Sort: {}".format(temp_l)
        # print "ordered_d is {}".format(ordered_d.items())
        loop_num2 = beam_width

        # if ordered_d.items().__len__() < beam_width:
        if temp_l.__len__() < beam_width:
            # loop_num2 = ordered_d.items().__len__()
            loop_num2 = temp_l.__len__()
        # print "loop_num2 is {}".format(loop_num2)
        # print "type of loop_num2 is : {}".format(type(loop_num2))

        j= 0

        # for j in range(0, loop_num2):
        while j<loop_num2:

            # q.put(ordered_d.items()[j][1]) # put the best beam_width paths into Queue
            # print "temp_l[j][1] is {}".format(temp_l[j][1])
            q.put(temp_l[j][1])
            # print "temp_l[j][1][-1] is: {}".format(temp_l[j][1][-1])
            # if ordered_d.items()[j][1][-1] == goal:
            if temp_l[j][1][-1] == goal:
                # return ordered_d.items()[j][1]
                return temp_l[j][1]
                # return ''.join(temp_l[j][1])
            else:
                # explored_nodes.add(ordered_d.items()[j][1][-1]) # put the last element of the best beam_width paths into explored set
                explored_nodes.add(temp_l[j][1][-1])
                # print "explored_nodes: {}".format(explored_nodes)
                j += 1
        qLen = q.queue.__len__()

    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    distance = 0
    if node_names.__len__() == 0: return distance
    for i in range(node_names.__len__() - 1):
        distance += graph.get_edge(node_names[i], node_names[i + 1]).length
    return distance
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    if start == goal:   return [start]
    q = Queue.PriorityQueue() # set up Q as PriorityQueue
    explored_nodes = set() # contain nodes that has been explored, avoiding loop
    q._put( (0, [start]) ) # put tuple (distance, list of nodes) into Queue

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
                q._put( (temp_dist, temp_l) )
                if v == goal:
                    return temp_l
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

HOW_MANY_HOURS_THIS_PSET_TOOK = '60'
WHAT_I_FOUND_INTERESTING = 'fixing bug'
WHAT_I_FOUND_BORING = 'fixing bug'
