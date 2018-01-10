from connectfour import *
from basicplayer import *
from util import *
import tree_searcher
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp = pp.pprint

board1 = ConnectFourBoard()
board2 = ConnectFourBoard()
print board1.do_move(1)
l = [1,2,3,4,1,2,3,2,3,2,3,4,5,6,5,3,4,3,2]
for i in l:
    # move = raw_input("enter int: ")
    board2 = board2.do_move(i)

print board1
print board2
# for i in board2.chain_cells(1):
#     print i

# print board2._chain_sets_from_cell(2,3).__len__()
# x= board2._chain_sets_from_cell(2,3)
# print x
# print filter(lambda y: y.__len__() >1, x)
x =board2.chain_cells(1)
pp(list(x))
pp(x)
print x
print "length of list(x): {}".format(x.__len__())
a = filter(lambda y: y.__len__() ==1, x)
pp(a)