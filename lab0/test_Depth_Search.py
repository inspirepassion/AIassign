count_depth = 0
def depth(expr):
    global count_depth
    def Depth_Recurssion(input):
        global count_depth
        for i in input:
            # print i
            if isinstance(i, (list, tuple)) == False:
                if (count_depth == 0):
                    count_depth = 1
                    return 1
            else:
                if 1+Depth_Recurssion(i) >= count_depth:
                    count_depth = 1+Depth_Recurssion(i)
                return 1+Depth_Recurssion(i)

    if isinstance(expr, (list, tuple)) == False:
       return count_depth
    else:
        Depth_Recurssion(expr)
    return count_depth

# print depth('x')
# print depth(('expt', 'x', 2))
print depth((('x')))
# print depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2))))


