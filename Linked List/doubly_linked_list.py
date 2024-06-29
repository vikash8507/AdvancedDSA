import random
from doubly_node import DoublyNode

class DoublyLinkedList:

    def __init__(self):
        self.head: DoublyNode = None
        self.tail: DoublyNode = None
        self.size: int = 0

    def create_doubly_linked_list(self, items):
        if not items:
            return self.head
        self.head = DoublyNode(items[0])
        self.tail = self.head
        self.size = 1
        for item in items[1:]:
            new_node = DoublyNode(item)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
    
    def random_node(self) -> DoublyNode:
        rand = random.randint(0, self.size-1)
        tmp = self.head
        for _ in range(1, rand):
            tmp = tmp.next
        return tmp

    @staticmethod
    def print(head: DoublyNode) -> None:
        tmp = head
        while tmp:
            print(tmp.data, end=" <==> ")
            tmp = tmp.next
        print()
