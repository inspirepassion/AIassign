from connectfour import *
from basicplayer import *
from util import *
import tree_searcher



board1 = ConnectFourBoard()
board2 = ConnectFourBoard()
print board1.do_move(1)
l = [1,2,3,4,1,2,3,2,3,2,3,4,5,6,5,3,4,3,2]
for i in l:
    # move = raw_input("enter int: ")
    board2 = board2.do_move(i)

print type(board2)
print board2.__repr__()

print type(get_all_next_moves(board2)), "\n ~~~~~~~~~~~~~~~"
print "length: {}".format(list(get_all_next_moves(board2)).__len__())
print list(get_all_next_moves(board2))