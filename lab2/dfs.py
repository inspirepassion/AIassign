from search import *
from graphs import *
import Queue

def main():
    print type(GRAPH1.nodes)
    # print(NEWGRAPH1.nodes)
    print "result is:\n{}".format(bfs(SAQG, 'S', 'G'))


    '''NEWGRAPH1, 'S', 'H
    answer:SCDH'''
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
if __name__ == "__main__":
    main()