"""
Delete middle of linked list

if the given linked list is 1->2->3->4->5 then the linked list should be modified to 1->2->4->5
 if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
"""
from linkedlist import LinkedList
from node import Node

def remove_middle(head: Node) -> Node:
    if head is None or head.next is None:
        return None
    if head.next.next is None:
        head.next = None
        return head
    slow = fast = head
    prev = None
    while fast.next and fast.next.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if fast.next is None:
        prev.next = slow.next
    else:
        slow.next = slow.next.next
    return head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 2, 3, 4, 5, 6])
    LinkedList.print_node_values_of_linked_list(head)
    head = remove_middle(head)
    LinkedList.print_node_values_of_linked_list(head)

main()
