from search import *
from graphs import *
import Queue

def main():
    print type(GRAPH1.nodes)
    # print(NEWGRAPH1.nodes)
    print "result is:\n{}".format(bfs(NEWGRAPH1, 'S', 'H'))


    '''NEWGRAPH1, 'S', 'H
    answer:SCDH'''
def bfs(graph, start, goal):
    if start == goal: return [start]
    dict_nodes = {}
    for node in graph.nodes:
        dict_nodes[node] = [0, None]

    result = []
    q = Queue.Queue()

    dict_nodes[start] = [1,None]
    q.put(start)
    while q.queue.__len__() != 0:
        u = q.get()
        for v in graph.get_connected_nodes(u):
            if dict_nodes[v][0] == 0:
                dict_nodes[v][0]=1
                if v is not start:
                    dict_nodes[v][1] = u
                if v == goal:
                    break
                else:
                    q.put(v)
                # q.put(v)
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





    # print "the 'Common Area's connected nodes are: {} ".format(GRAPH1.get_connected_nodes('Common Area'))

    #
    # q=Queue.Queue()
    #
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # for i in q.queue:
    #     print i
    # print "the get returns {}".format(q.get())
    # for i in q.queue:
    #     print i
    # q.get()
    # q.put(4)
    # print "\n"
    # for i in q.queue:
    #     print i
    # print (q.queue.__len__())
    '''
    for i in range(1,14,2):
        q.put(i)

    q.put('a')
    q.get()
    q.put('b')

    print type(q)
    print q
    for i in q.queue:
        print i'''


GRAPH1 = Graph(edgesdict = \
               [{NAME:'e1',  VAL: 5, NODE1:'Common Area', NODE2:'Stairs'},
                {NAME:'e2',  VAL:15, NODE1:'Entrance Hall', NODE2:'Hospital'},
                {NAME:'e3',  VAL: 7, NODE1:'Classroom 11', NODE2:'Hospital'},
                {NAME:'e4',  VAL:25, NODE1:'Haunted Bathroom', NODE2:'The Chamber'},
                {NAME:'e5',  VAL: 5, NODE1:'Forbidden Area', NODE2:'Trophy Room'},
                {NAME:'e6',  VAL: 3, NODE1:'Mirrored Room', NODE2:'Statues'},
                {NAME:'e7',  VAL: 1, NODE1:'Grand Hall', NODE2:'Entrance Hall'},
                {NAME:'e8',  VAL: 4, NODE1:'Dungeon 5', NODE2:'Haunted Bathroom'},
                {NAME:'e9',  VAL: 2, NODE1:'Stairs', NODE2:'Grand Hall' },
                {NAME:'e10', VAL: 9, NODE1:'Statues', NODE2:'Stairs' },
                {NAME:'e11', VAL: 6, NODE1:'Entrance Hall', NODE2:'Haunted Bathroom' },
                {NAME:'e12', VAL: 4, NODE1:'Forbidden Area', NODE2:'Stairs' },
                {NAME:'e13', VAL:10, NODE1:'Classroom 11', NODE2:'Entrance Hall' },
                {NAME:'e14', VAL: 5, NODE1:'Trophy Room', NODE2:'Stairs' },
                {NAME:'e15', VAL: 8, NODE1:'Stairs', NODE2:'Mirrored Room' },
                {NAME:'e16', VAL: 3, NODE1:'Entrance Hall', NODE2:'Stairs' },
                {NAME:'e17', VAL: 8, NODE1:'Necessary Room', NODE2:'Common Area'}
                ],
               heuristic = \
               {'Common Area':
                    {'Hospital':17,
                     'Classroom 11':10,
                     'Entrance Hall':7,
                     'Haunted Bathroom':13,
                     'Dungeon 5':15,
                     'The Chamber':14,
                     'Forbidden Area':8,
                     'Trophy Room':6,
                     'Stairs':4,
                     'Grand Hall':6,
                     'Common Area':0,
                     'Statues':12,
                     'Mirrored Room':10,
                     'Necessary Room':6 }})

if __name__ == "__main__":
    main()