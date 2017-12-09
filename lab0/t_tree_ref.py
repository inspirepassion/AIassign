def tree_ref(tree, index):
    if isinstance(tree, (tuple, list)) == False:
        return tree
    elif len(index)==0:
        return tree
    else:
        return tree_ref(tree[index[0]], index[1:])

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print tree_ref(tree, (1,1,1))

