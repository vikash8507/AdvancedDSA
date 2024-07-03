from random import randint

def get_random_array(size: int):
    lst = []
    for _ in range(size):
        lst.append(randint(1, 100))
    return lst
