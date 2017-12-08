

def depth(expr):
    initNum = -1

    def Depth_Recurssion(enter):
        if isinstance(enter, (list, tuple)) == False:
                return 1
        else:
            elem_list = [None]*len(enter)
            for i,j in enumerate(enter):
                elem_list[i] = 1+Depth_Recurssion(j)
            elem_list.sort(reverse=True)
            return elem_list[0]
    return Depth_Recurssion(expr) + initNum

print depth('x')
# print depth(('expt', 'x', 2))
print "The Algo: %d" %depth((('x', 'y' , 'z'), 10))
print depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2))))

