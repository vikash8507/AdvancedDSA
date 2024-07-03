"""
Given an array of N elements. Count the number of duplicate pair of elements
    - (i, j): A[i] == A[j] and i<j
    - TC O(N) and SC O(N)
    INPUT:- 1, 2, 1, 4, 1, 2, 3, 4, 1, 6
    OUTPUT:- 8
    Use HashMap or HashSet
"""

def count_paris(lst):
    answer = 0
    dct = {}
    for item in lst:
        current_count = dct.get(item, 0)
        answer += current_count
        dct.update({item: current_count + 1})
    return answer


lst = [1, 2, 1, 4, 1, 2, 3, 4, 1, 6]
print(count_paris(lst))

