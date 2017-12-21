from search import *
from graphs import *
from collections import *

def main():
    # print "Heuristic info: {}".format(GRAPH1.get_heuristic( 'Hospital','Common Area'))
    # d = dict(d = 3, a=1, b=2, c=3, e=3)
    # dd = {11: 1,12: 2, 14: 3, 13: 3,  15:3}
    # print type(d)
    # for i in d.items():
    #     print i
    #
    # print type(d.items())
    # print dd.items()

    l = ["Hospital", "Classroom 11", "Entrance Hall"]
    d = {i:GRAPH1.get_heuristic(i, "Common Area") for i in l}
    # [('Hospital', 17), ('Classroom 11', 10), ('Entrance Hall', 7)]
    print d.items()
    ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print ordered_d.items()

    l2 = [1,2]
    for i in ordered_d.items():
        l2 = l2+[i[0]]
    print l2
    # sorted(dd.items(), key=lambda x: (x[1],x[0]), reverse=False)
    # print dd.items()


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