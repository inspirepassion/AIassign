def count_pattern(pattern, lst):
    num_of_pattern =0
    len_of_pattern = len(pattern)
    len_of_lst = len(lst)
    index_of_firstElement = [i for i, j in enumerate(lst[:len_of_lst-len_of_pattern+1]) if pattern[0] == j]
    print index_of_firstElement


'''def find_index_ofFirstLetter(pattern, lst)
'''

print(count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')))