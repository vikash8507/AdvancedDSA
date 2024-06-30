"""
Input : 1->2->3->4->5->6->NULL 
Output : 2->1->4->3->6->5->NULL

Input : 1->2->3->4->5->NULL 
Output : 2->1->4->3->5->NULL

Input : 1->NULL 
Output : 1->NULL 
"""

from node import Node
from linkedlist import LinkedList

def pair_wise_swap(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    current = head
    while current and current.next:
        tmp = current.data
        current.data = current.next.data
        current.next.data = tmp
        current = current.next.next
    return head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 2, 3, 4, 5, 6])
    LinkedList.print_node_values_of_linked_list(head)
    head = pair_wise_swap(head)
    LinkedList.print_node_values_of_linked_list(head)

main()
