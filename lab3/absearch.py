from tree_searcher import *

from connectfour import *
from basicplayer import *
from util import *
import tree_searcher




def fn_ab(board, depth, eval_fn, get_next_moves_fn=get_all_next_moves, is_terminal_fn=is_terminal):

    def fn(node_type=None, cp_root={"type": None, "value": None}, board=board, depth=depth, eval_fn=eval_fn,
           get_next_moves_fn=get_next_moves_fn, is_terminal_fn=is_terminal_fn):
        if node_type == "MAX":
            node_type="MIN"
        else:
            node_type = "MAX"
        print "\nin absearch.py: board type: {}".format(type(board))
        if is_terminal_fn(depth, board):
            b = eval_fn(depth, board)
            return (b, board)
        children = list(get_next_moves_fn(board))
        child_count = children.__len__()
        alpha = (None, None)
        for i in range(child_count):
            import tree_searcher
            temp_val_tup = fn(node_type, cp_root, make_tree(children[i]), depth-1, is_terminal_fn, eval_fn)
            print "temp_val_tup: {}".format(temp_val_tup)
            temp_val = temp_val_tup[0]
            print "temp_val: {}".format(temp_val)
            val = -1 * temp_val
            if cp_root["type"] != None and cp_root["type"] != node_type and -val < cp_root["value"]:
                alpha = (-1 * cp_root["value"], None)
                break
            if alpha[0] == None or val > alpha[0]:
                alpha = (val, children[i])
                cp_root["value"] = alpha[0]
        return alpha

    initial_type = "MIN"

    fn(node_type=initial_type, board = board)
    # fn(node_type=initial_type, cp_root={"type": None, "value": None}, board=board, depth=depth, eval_fn=eval_fn,
    #    get_next_moves_fn=get_next_moves_fn, is_terminal_fn=is_terminal_fn)
    print "\n finish \n"


