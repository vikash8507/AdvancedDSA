"""
Given a Y-shaped Linked List. Find intersection Node.
"""
from node import Node
from linkedlist import LinkedList


def linked_list_node_counts(head: Node) -> int:
    count = 0
    tmp = head
    while tmp:
        tmp = tmp.next
        count += 1
    return count


def find_intersection_point(head1: Node, head2: Node) -> Node:
    count1 = linked_list_node_counts(head1)
    count2 = linked_list_node_counts(head2)
    tmp1 = head1
    tmp2 = head2
    if count1 > count2:
        for _ in range(count1-count2):
            tmp1 = tmp1.next
    else:
        for _ in range(count2-count1):
            tmp2 = tmp2.next
    while tmp1 and tmp2:
        if tmp1 == tmp2:
            return tmp2
        tmp1 = tmp1.next
        tmp2 = tmp2.next
    return None


def main():
    ll1 = LinkedList()
    head1 = ll1.create_linked_list_with_list([15, 3, 5, 7, 8, 9])
    ll2 = LinkedList()
    head2 = ll2.create_linked_list_with_list([16, 10, 11])
    ll3 = LinkedList()
    head3 = ll3.create_linked_list_with_list([1, 3, 4])
    ll1.tail.next = head3
    ll2.tail.next = head3

    LinkedList.print_node_values_of_linked_list(head1)
    LinkedList.print_node_values_of_linked_list(head2)

    intersection_node = find_intersection_point(head1, head2)
    print(intersection_node.data)


main()
