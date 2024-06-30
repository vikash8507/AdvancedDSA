"""
Delete last occurrence of an item from linked list

Created Linked list: 1 --> 2 --> 3 --> 4 --> 5 --> 4 --> 4 --> NULL
List after deletion of 4: 1 --> 2 --> 3 --> 4 --> 5 --> 4 --> NULL

Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10


"""
from node import Node
from linkedlist import LinkedList


def delete_last_occurance_of_item(head: Node, target_item: int) -> Node:
    if head is None or head.next is None:
        return head
    tmp = head
    prev, target_prev = None, None
    target = None
    while tmp:
        if tmp.data == target_item:
            target_prev = prev
            target = tmp
        prev = tmp
        tmp = tmp.next
    if prev == head and target:
        return head.next
    if target:
        target_prev.next = target_prev.next.next
    return head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 2, 3, 5, 2, 10])
    LinkedList.print_node_values_of_linked_list(head)
    head = delete_last_occurance_of_item(head, 2)
    LinkedList.print_node_values_of_linked_list(head)

main()
    

