"""
Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL 
Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL

Input: 1 -> 1 -> 2 -> 1 -> 0 -> NULL 
Output: 0 -> 1 -> 1 -> 1 -> 2 -> NULL 
"""
from linkedlist import LinkedList
from node import Node


def sort_012(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    count0, count1, count2 = [0, 0, 0]
    tmp = head
    while tmp:
        if tmp.data == 0:
            count0 += 1
        elif tmp.data == 1:
            count1 += 1
        else:
            count2 += 1
        tmp = tmp.next
            
    tmp = head
    for _ in range(count0):
        tmp.data = 0
        tmp = tmp.next
    for _ in range(count1):
        tmp.data = 1
        tmp = tmp.next
    for _ in range(count2):
        tmp.data = 2
        tmp = tmp.next
    return head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 1, 2, 1, 0])
    LinkedList.print_node_values_of_linked_list(head)
    head = sort_012(head)
    LinkedList.print_node_values_of_linked_list(head)

main()
