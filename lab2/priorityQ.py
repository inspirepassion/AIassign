import Queue

q = Queue.PriorityQueue()

print type(q)
print(q.queue)
q._put((6,4,'f'))
q._put((2,1,'c'))
q._put((8, 5, 'a'))
q._put((3, 10, 'b'))
q._put((9, 6, 'd'))
print(q.queue)
q._get()
print(q.queue)
q._put((8, 2,'f'))
print(q.queue)
print "q._get(): {}".format(q._get())
print(q.queue)
print q.queue.__len__()