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


def main():
    ll = LinkedList()
    head = ll.create_node_of_size_n(5)
    LinkedList.print_node_values_of_linked_list(head)
    head = reverse_linked_list(head)
    print()
    LinkedList.print_node_values_of_linked_list(head)

main()
