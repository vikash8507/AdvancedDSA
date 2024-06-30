"""
Input: linked list = 10->20->30->40->50->60, k = 4
Output: 50->60->10->20->30->40. 
Explanation: k is smaller than the count of nodes in a linked list so (k+1 )th node i.e. 50 becomes the head node and 60's next points to 10

Input: linked list = 30->40->50->60, k = 2
Output: 50->60->30->40. 
"""

from linkedlist import LinkedList
from node import Node

def rotate_linked_list(head: Node, k: int) -> Node:
    if head is None or k <= 0:
        return head
    tmp = head
    i = 1
    while tmp and i != k:
        tmp = tmp.next
        i += 1
    if tmp is None or tmp.next is None:
        return head
    new_head = tmp.next
    tmp.next = None
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head
    return new_head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([30, 40, 50, 60])
    LinkedList.print_node_values_of_linked_list(head)
    head = rotate_linked_list(head, 2)
    LinkedList.print_node_values_of_linked_list(head)

main()
