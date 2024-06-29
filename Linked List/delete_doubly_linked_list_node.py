from doubly_linked_list import DoublyLinkedList
from doubly_node import DoublyNode

def delete_given_node(head: DoublyNode, tail: DoublyNode, node: DoublyNode) -> DoublyNode:
    if node == head:
        head = head.next
        head.prev = None
    elif node == tail:
        node.prev.next = None
        node.prev = None
    else:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    return head


def main():
    dll = DoublyLinkedList()
    dll.create_doubly_linked_list([8, 2, 3, 4, 5, 6, 0])
    random_node = dll.random_node()
    head, tail = dll.head, dll.tail
    DoublyLinkedList.print(head)
    print(random_node.data)
    head = delete_given_node(head, tail, random_node)
    DoublyLinkedList.print(head)

main()
