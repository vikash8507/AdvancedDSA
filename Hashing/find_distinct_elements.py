"""
Input: [1, 2, 4, 5, 1, 5, 7, 2, 5]
Output: 5
"""

from util import get_random_array


def find_total_distinct(items):
    st = set()
    for item in items:
        st.add(item)
    return len(st)

lst = get_random_array(50)
print(find_total_distinct(lst))
