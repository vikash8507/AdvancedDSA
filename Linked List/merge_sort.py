from node import Node
from linkedlist import LinkedList
from questions_set1 import find_middlemost_element_linked_list
from merge_sorted_linked_list import merge_two_sorted_linked

def mergeSort(head: Node):
    if head is None or head.next is None:
        return head
    middle = find_middlemost_element_linked_list(head)
    head1 = middle.next
    middle.next = None
    head = mergeSort(head)
    head1 = mergeSort(head1)
    head = merge_two_sorted_linked(head, head1)
    return head

def main():
    ll = LinkedList()
    head = ll.create_node_of_size_n(6)
    LinkedList.print_node_values_of_linked_list(head)
    print()
    sortedLL = mergeSort(head)
    LinkedList.print_node_values_of_linked_list(sortedLL)

main()
