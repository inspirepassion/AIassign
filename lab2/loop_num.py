from collections import *
i =3
for i in range(5):
    print i, "in for loop"
print "i is: {}".format(i)

d = dict(a=1, e=2, s=5, b=9, c=3)
print d

ordered_d = OrderedDict(sorted(d.items(), key=lambda x: x[0], reverse=True))

print ordered_d
print type(ordered_d)
print ordered_d.items().__len__()

print ordered_d.items()[1]