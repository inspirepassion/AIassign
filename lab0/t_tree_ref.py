def t_tree_ref(tree, index):
    if isinstance(tree, (tuple, list)) == False:
        return tree
    elif len(index) == 1:
        return tree
    else:
        return t_tree_ref(tree[index[0]], index.pop(0))

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print(t_tree_ref(tree, (3,1)))