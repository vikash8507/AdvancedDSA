from node import Node
from linkedlist import LinkedList


def detect_cycle(head: Node) -> bool:
    if head is None:
        return False
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    ll = LinkedList()
    linear_head = ll.create_node_of_size_n(5)
    print(detect_cycle(linear_head), "====================")
    cyclic_head = ll.create_cyclic_linked_list(5)
    print(detect_cycle(cyclic_head), "============================")

# main()
