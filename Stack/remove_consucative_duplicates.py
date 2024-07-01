"""
Given a string. Remove every consucative dublicate pair of chars until there are no consucative duplicate pair.
s = "acddck"
out -> "ak"

s = "abckkcbadmmc"
out -> "dc"
"""
from stack import StackWithLinkedList


def remove_consucative_duplicates(string):
    stack = StackWithLinkedList()
    for chr in string:
        if stack.peak() == chr:
            stack.pop()
        else:
            stack.push(chr)
    return stack.to_string()

def main():
    string = "acddck"
    result = remove_consucative_duplicates(string)
    print(result, "==================")

    string = "abckkcbadmmc"
    result = remove_consucative_duplicates(string)
    print(result, "==================")

main()
