def func(**args):
    class BindArgs(object):
       foo = args['foo']
       print 'foo is ', foo
       def __init__(self,args):
           print "hello i am here"
    return BindArgs(args)  # return an instance of the class

f = func(foo=2)