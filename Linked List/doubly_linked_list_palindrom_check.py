from doubly_linked_list import DoublyLinkedList
from doubly_node import DoublyNode

def check_palindrom(head: DoublyNode, tail: DoublyNode) -> bool:
    if head is None or head ==  tail:
        return True
    h, t = head, tail
    while h != t and h.prev != t:
        if h.data != t.data:
            return False
        h = h.next
        t = t.prev
    return True

def main():
    dll = DoublyLinkedList()
    dll.create_doubly_linked_list([1, 3, 3, 1])
    head, tail = dll.head, dll.tail
    print(check_palindrom(head, tail))

main()
