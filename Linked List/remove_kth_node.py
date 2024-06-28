"""
Input : 1->2->3->4->5->6->7->8  
        k = 3
Output : 1->2->4->5->7->8
As 3 is the k-th node after its deletion list 
would be 1->2->4->5->6->7->8
And now 4 is the starting node then from it, 6 
would be the k-th node. So no other kth node 
could be there.So, final list is:
1->2->4->5->7->8.

Input: 1->2->3->4->5->6  
       k = 1
Output: Empty list 
All nodes need to be deleted
"""
from node import Node
from linkedlist import LinkedList

def remove_kth_node(head: Node, k: int) -> Node:
    if head is None or head.next is None or k == 0:
        return head
    if k == 1:
        return None
    i = 1
    tmp = head
    while tmp:
        if i == k-1:
            if tmp.next:
                tmp.next = tmp.next.next
            else:
                tmp.next = None
            i = 0
        tmp = tmp.next
        i += 1
    return head


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 2, 3, 4, 5, 6, 7, 8])
    LinkedList.print_node_values_of_linked_list(head)
    head = remove_kth_node(head, 3)
    LinkedList.print_node_values_of_linked_list(head)

main()

