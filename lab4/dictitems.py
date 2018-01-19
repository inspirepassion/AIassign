d = dict([('a', 1), ('b', 2), (3, 'c')])
print d
for i in d.items():
    print i

print "if 'a' in d: {}".format('a' in d)
print "if 2 in d: {}".format(2 in d)
print "if 3 in d: {}".format(3 in d)