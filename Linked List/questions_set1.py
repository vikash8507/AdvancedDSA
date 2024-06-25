# Reverse a Linked List
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

from node import Node
from linkedlist import LinkedList

def reverse_linked_list(head: Node):
    if head is None or head.next is None:
        return head
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head

# Find middlemost element of Linked List
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 3
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# Output: 3 / 4


def find_middlemost_element_linked_list(head: Node):
    if head is None:
        return None, None
    if head.next is None:
        return head.data, None
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    if fast.next is None:
        return slow.data, None
    return slow.data, slow.next.data


def main():
    ll = LinkedList()
    head = ll.create_node_of_size_n(0)
    LinkedList.print_node_values_of_linked_list(head)
    print()
    # head = reverse_linked_list(head)
    # LinkedList.print_node_values_of_linked_list(head)
    print(find_middlemost_element_linked_list(head), "=============================")

main()
