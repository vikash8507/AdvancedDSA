from typing import Any
from random import randint

class Node:
    def __init__(self, data, next = None) -> None:
        self.data: Any = data
        self.next: Node | None = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def create_node_of_size_n(self, size):
        if not isinstance(size, int) or size < 1:
            raise ValueError
        self.head = Node(randint(1, 100))
        self.tail = self.head
        for _ in range(1, size):
            new_node = Node(randint(1, 100))
            self.tail.next = new_node
            self.tail = new_node
        return self.head

    @staticmethod
    def print_node_values_of_linked_list(head: Node) -> Node:
        if head is None:
            return head
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


ll = LinkedList()
head = ll.create_node_of_size_n(5)
LinkedList.print_node_values_of_linked_list(head)
c = LinkedList.count_linked_list_nodes(head)
print()
print(c, "===============Count")
k = randint(0, c-1)
kth = LinkedList.node_at_kth_position(head, k)
if kth:
    print(kth.data, f"Data at {k}")
else:
    print("Wrong k")