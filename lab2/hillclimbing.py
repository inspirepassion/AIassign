from search import *
from graphs import *
import Queue
from collections import *

def main():
    print type(GRAPH1.nodes)
    # print(NEWGRAPH1.nodes)
    print "result is:\n{}".format(hill_climbing(NEWGRAPH1, 'S', 'G'))
    # 'SABDCEG'


    '''NEWGRAPH1, 'S', 'H
    answer:SCDH'''
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
        print "before pop, stack: {}".format(stack)
        u = stack.pop()
        dict_nodes[u][0] = 2 # mark as black, the node is chosen to be explored
        heuristic_List = []
        print "heuristic_List before for(): {}".format(heuristic_List)
        for v in graph.get_connected_nodes(u):
            print "u is: {}".format(u)
            print "v is: {}".format(v)

            # if dict_nodes[v][0] == 0:
            if dict_nodes[v][0] != 2 and v is not start:
                dict_nodes[v][0]=1
                # print "check out v in if: {}".format(v)
                if v is not start:
                    dict_nodes[v][1] = u
                if v == goal:
                    break
                else:
                    # print "v: right in front append: {}".format(v)
                    heuristic_List.append(v) # put children into temperary list for sorting heuristic info
                    # print "check out each v appended into heuristic_list: {}".format(v)
                # stack.append(v)

        # put stack elements into heuristic_List
        heuristic_List = stack + heuristic_List

        # sorting elements in heuristic list:
        print type(heuristic_List)
        print "heuristic_List is: ", heuristic_List
        print "items in heuristic_List: {}".format(heuristic_List)
        d = {i:graph.get_heuristic(i,goal) for i in heuristic_List}
        print "Check dictionary creation: {}".format(d.items())
        ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        stack = [] # the only change
        for i in ordered_d.items():
            stack.append(i[0])
        print "Check out stack for each round: {}".format(stack)

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
        return ''.join(result)
if __name__ == "__main__":
    main()