"""
Check a Given Singly Linked List is Palindrom or not
SLL - 1 -> 2 -> 1
Out - true
SLL - 1 -> 2
Out - false
"""
from node import Node
from linkedlist import LinkedList


def split_list_from_middle(head: Node) -> list[Node, Node]:
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    head1 = slow.next
    return [head, head1]


def reverse_linked_list(head: Node) -> Node:
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def check_palindrom(head: Node) -> bool:
    if head is None or head.next is None:
        return True
    head1, head2 = split_list_from_middle(head)
    head2 = reverse_linked_list(head2)

    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next

    return True


def main():
    ll = LinkedList()
    head = ll.create_linked_list_with_list([1, 2, 1, 1])
    is_palindrom = check_palindrom(head)
    print("Palindrom" if is_palindrom else "Not Palindrom")


main()
