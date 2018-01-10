if not 'set' in globals():
    from sets import Set as set
s= set()
s = {(1, 2, 3), (2, 3)}
s.update([((9,1),(1,0)), ((1,2),(2,3))])
print s
