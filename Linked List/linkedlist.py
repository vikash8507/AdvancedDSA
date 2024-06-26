from random import randint
from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def create_node_of_size_n(self, size):
        if not isinstance(size, int) or size < 0:
            raise ValueError
        if size == 0:
            return
        self.head = Node(randint(1, 100))
        self.tail = self.head
        for _ in range(1, size):
            new_node = Node(randint(1, 100))
            self.tail.next = new_node
            self.tail = new_node
        return self.head

    def create_cyclic_linked_list(self, size):
        self.head = self.create_node_of_size_n(size)
        self.tail.next = self.head
        return self.head


    def sorted_linked_list_generation(self, size):
        if size < 1:
            return
        items = [randint(1, 100) for _ in range(size)]
        items.sort()

        self.head = self.tail = Node(items[0])
        for item in items[1:]:
            new_node = Node(item)
            self.tail.next = new_node
            self.tail = new_node
        return self.head


    @staticmethod
    def print_node_values_of_linked_list(head: Node) -> Node:
        if head:
            temp = head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
        return head

    @staticmethod
    def count_linked_list_nodes(head: Node) -> int:
        count: int = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count

    @staticmethod
    def node_at_kth_position(head: Node, k: int) -> Node | None:
        if k < 0 or head is None:
            return
        temp = head
        while k > 0 and temp:
            temp = temp.next
            k -= 1
        return temp
