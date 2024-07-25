"""
Given an array. Find the nearest smaller element on left side for every elements

I/P: {1, 6, 4, 10, 2, 5}
O/P: {_, 1, 1,  4, 1, 2}

I/P: {1, 3, 0, 2, 5}
O/P: {_, 1, _, 0, 2}

"""


def find_nearest_smaller_left(items):
    l = len(items)
    result = ["_"]*l
    stack = []
    sl = 0

    for i  in range(l):
        while sl != 0 and stack[-1] >= items[i]:
            stack.pop()
            sl -= 1
        if sl != 0:
            result[i] = stack[-1]
        stack.append(items[i])
        sl += 1
    return result

print(find_nearest_smaller_left([1, 3, 0, 2, 5]))
