"""
Given an array. Find the nearest smaller element's index on left side for every elements

I/P: {1, 6, 4, 10, 2, 5}
O/P: {-1, 0, 0,  2, 0, 4}

I/P: {1, 3, 0, 2, 5}
O/P: {-1, 0, -1, 2, 3}
"""


def find_nearest_smaller_left_element_index(items):
    l = len(items)
    result = [-1]*l
    stack = []
    sl = 0

    for i in range(l):
        while sl != 0 and items[stack[-1]] >= items[i]:
            stack.pop()
            sl -= 1
        if sl != 0:
            result[i] = stack[-1]
        stack.append(i)
        sl += 1

    return result

print(find_nearest_smaller_left_element_index([1, 6, 4, 10, 2, 5]))
