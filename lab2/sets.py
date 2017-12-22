from collections import *
import Queue

q = Queue.Queue()


s = set()
print type(s)
s.add('a')
s.add('b')
if 'c' not in s:
    print "c is not in s"
print s
print 'c' in s

d = dict(a=1,f=9,b=4)
# print d
# d['a'] = 3
# print d
tl = [('a',1), ('f', 9),('a',2), ('b',4), ('c',1)]
print tl
print tl.sort(key=lambda x: x[1])
print tl
print tl.__len__()
print tl[1][0]
ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))

l = ['a']
print l
l.append('b')
print l

# print type(d.items())
# print d.items()
#
# print type(ordered_d.items())
# print ordered_d.items()
#
# print ordered_d.items()[1]
#
# print ordered_d.items()[1][0] == 'b'

# l = [1,2]
# l2 = ['a','b']
# print l[-1]
#
# d[1] = l
#
# print d
#
# q.put(l)
# q.put(l2)
# print q.queue
#
# for i in range(0,2):
#     print i
