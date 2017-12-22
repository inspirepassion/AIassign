from graphs import *
from search import *
import Queue
from collections import *

def main():
    # beam_search(NEWGRAPH1, 'F', 'G', 2)
    print "Running Result: {}".format(beam_search(NEWGRAPH1, 'F', 'G', 2))
    # NEWGRAPH1, 'F', 'G', 2
    #'FBASCEG'


def beam_search(graph, start, goal, beam_width):
    if start == goal: return [start]

    q = Queue.Queue()
    explored_nodes = set()

    q.put([start]) # Enqueue each elements in Queue as a list of nodes
    explored_nodes.add(start)
    qLen = q.queue.__len__()
    while qLen != 0:


        loop_num = beam_width
        print "\nloop_num is {}".format(loop_num)
        print "Queue is: {}".format(q.queue)
        print "q.queue.__len__(): {}".format(q.queue.__len__())

        if qLen < beam_width:
            loop_num = qLen

        temp_l = []
        for i in range(loop_num):
            print "\nloop_num is {}".format(loop_num)
            u = q.get() # As each element in Queue is a list of nodes, this gets the list, Note that the last node in the list q.get()[-1]


            print "\nu is {}\nAdjacents is {}".format(u[-1], graph.get_connected_nodes(u[-1]))
            print "num_children is {}".format(graph.get_connected_nodes(u[-1]).__len__())
            print "Before for loop, the explored_nodes: {}".format(explored_nodes)
            for v in graph.get_connected_nodes(u[-1]):
                if v not in explored_nodes:

                    print "u is {}".format(u)
                    print "in this loop, v is {}".format(v)
                    temp = u[:] # assign value of u to temp
                    temp.append(v)
                    temp_l.append((graph.get_heuristic(v,goal), temp))
                    # print "temp_l is {}".format(temp_l)
            print "After for loop, the explored_nodes: {}".format(explored_nodes)
        # Sort elements in temperary dictionary, such that we could choose the best beam_width elements into Queue
        # ordered_d = OrderedDict(sorted(temp_d.items(), key = lambda x: x[0]))
        temp_l.sort(key=lambda x: x[0])
        print "Sort: {}".format(temp_l)
        # print "ordered_d is {}".format(ordered_d.items())
        loop_num2 = beam_width

        # if ordered_d.items().__len__() < beam_width:
        if temp_l.__len__() < beam_width:
            # loop_num2 = ordered_d.items().__len__()
            loop_num2 = temp_l.__len__()
        print "loop_num2 is {}".format(loop_num2)
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
            else:
                # explored_nodes.add(ordered_d.items()[j][1][-1]) # put the last element of the best beam_width paths into explored set
                explored_nodes.add(temp_l[j][1][-1])
                print "explored_nodes: {}".format(explored_nodes)
                j += 1
        qLen = q.queue.__len__()


if __name__ == "__main__":
    main()