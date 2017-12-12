from itertools import izip

lst = [1,2,3,4,5,6,7,8,9]
# def pairwise(iterable):
#     "s -> (s0, s1), (s2, s3), (s4, s5), ..."
#     a = iter(iterable)
#     return izip(a, a)
# #
# # for x, y in pairwise(lst):
# #    print "%d + %d = %d" % (x, y, x + y)
#
# for i in pairwise(lst):
#     print i
#

lst = [1,2,3,4,5,6,7,8,9]

from itertools import izip
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def func(s, nums):
    if len(nums) % 2 == 1:
        nums.append(0)
    if max(nums) >= s:
        return 1
    else:
        templst = map(lambda x: x[0]+x[1], pairwise(nums))
        return func(s, templst)+1

print func(17, lst)
