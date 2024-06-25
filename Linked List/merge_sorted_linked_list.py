from node import  Node
from linkedlist import LinkedList


def merge_two_sorted_linked(head1: Node, head2: Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    head = Node(-1)
    temp = head
    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            temp = temp.next
            head1 = head1.next
        else:
            temp.next = head2
            temp = temp.next
            head2 = head2.next
    if head1:
        temp.next = head1
    if head2:
        temp.next = head2
    head = head.next
    return head.next


def main():
    ll = LinkedList()
    head1 = ll.sorted_linked_list_generation(5)
    LinkedList.print_node_values_of_linked_list(head1)
    print()
    head2 = ll.sorted_linked_list_generation(5)
    LinkedList.print_node_values_of_linked_list(head2)
    print()
    head = merge_two_sorted_linked(head1, head2)
    LinkedList.print_node_values_of_linked_list(head)
    print()

# main()
