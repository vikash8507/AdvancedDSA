"""
Merge Two Sorted Stack into One Sorted Stack
stack1 1 -> 2 -> 5
stack2 3 -> 4 -> 6
Out 1 -> 2 -> 3 -> 4 -> 5 -> 6
"""


from stack import StackWithLinkedList


def merge_two_sorted_stacks(stack1: StackWithLinkedList, stack2: StackWithLinkedList) -> StackWithLinkedList:
    stack = StackWithLinkedList()
    while not stack1.is_empty() and not stack2.is_empty():
        if stack1.peak() > stack2.peak():
            stack.push(stack1.pop())
        else:
            stack.push(stack2.pop())

    while not stack1.is_empty():
        stack.push(stack1.pop())

    while not stack2.is_empty():
        stack.push(stack2.pop())

    return stack


def main():
    stack1 = StackWithLinkedList()
    stack1.generate_stack([1, 2, 5])
    stack1.print()
    stack2 = StackWithLinkedList()
    stack2.generate_stack([3, 4, 6])
    stack2.print()
    stack = merge_two_sorted_stacks(stack1, stack2)
    stack.print()


main()
