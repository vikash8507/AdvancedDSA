from doubly_node import DoublyNode
from doubly_linked_list import DoublyLinkedList


def insert_node_before_given_node(head: DoublyNode, node: DoublyNode, item: int) -> DoublyNode:
    new_node = DoublyNode(item)
    if node == head:
        new_node.next = head
        head.prev = new_node
        head = new_node
    else:
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
    return head

def insert_node_after_given_node(head: DoublyNode, tail: DoublyNode, node: DoublyNode, item: int) -> DoublyNode:
    new_node = DoublyNode(item)
    if node == tail:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node
    else:
        new_node.next = node.next
        node.next.prev = new_node
        new_node.prev = node
        node.next = new_node
    return head


def main():
    dll = DoublyLinkedList()
    dll.create_doubly_linked_list([8, 2, 3, 4, 5, 6, 0])
    random_node = dll.random_node()
    head, tail = dll.head, dll.tail
    DoublyLinkedList.print(head)
    print(random_node.data)
    # head = insert_node_before_given_node(head, random_node, 1)
    head = insert_node_after_given_node(head, tail, random_node, 9)
    DoublyLinkedList.print(head)

# main()
