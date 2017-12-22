from graphs import *
from search import *
import Queue
from collections import *

def main():
    # beam_search(NEWGRAPH1, 'F', 'G', 2)
    print "Running Result: {}".format(beam_search(NEWGRAPH1, 'F', 'G', 2))
    # NEWGRAPH1, 'F', 'G', 2
    #'FBASCEG'

    # NEWGRAPH1, 'F', 'G', 10
    # 'FBDEG'

def beam_search(graph, start, goal, beam_width):
    if start == goal: return [start]
    dict_nodes = {}
    for node in graph.nodes:
        dict_nodes[node] = [0, None]

    result = []
    q = Queue.Queue()

    #start
    dict_nodes[start][0] = 1
    q.put(start)
    # print q.queue.__len__()
    while q.queue.__len__() != 0:
        temp_list = [] # list that will contain all elements for each level
        loop_num = beam_width
        if q.queue.__len__() < beam_width:
            loop_num = q.queue.__len__()
        for i in range(loop_num):
            u=q.get()
            dict_nodes[u][0] = 2
            if goal in temp_list:
                break
            for v in graph.get_connected_nodes(u):
                if dict_nodes[v][0] != 2:
                    dict_nodes[v][1] = u
                    dict_nodes[v][0] = 1
                    temp_list.append(v)
                    if v == goal:
                        break

        # Sort beam_width number of nodes into Queue
        d = {j: graph.get_heuristic(j, goal) for j in temp_list}
        ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
        # loop through to Enqueue, using if to handle the case where there is less nodes then beam_width
        loop_num2 = beam_width
        if ordered_d.items().__len__() < beam_width:
            loop_num2 = ordered_d.items().__len__()
        for i in range(loop_num2):
            q.put(ordered_d.items()[i][0])
        # print "Queue: {}".format(q.queue)

    # return result by following the linked parents between nodes
    if dict_nodes[goal][1] == None:
        return result

    else:
        link = dict_nodes[goal][1]
        result.append(goal)
        while link is not start:
            # print "While Loop: link is: {}".format(link)
            result.insert(0, link)
            link = dict_nodes[link][1]
        result.insert(0, start)

        # return type(result)
        return ''.join(result)


if __name__ == "__main__":
    main()