from node import Node
from linkedlist import LinkedList

def detect_cycle_point(head: Node) -> Node:
    if head.next == head:
        return head
    if head is None or head.next is None:
        return None
    slow = fast = head
    meet_point = None
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            meet_point = slow
            break
    if meet_point:
        if meet_point == head:
            return head
        temp = head
        while temp and meet_point:
            temp = temp.next
            meet_point = meet_point.next
            if temp == meet_point:
                return meet_point


def main():
    ll = LinkedList()
    linear_head = ll.create_node_of_size_n(5)
    print(detect_cycle_point(linear_head), "====================")
    cyclic_head = ll.create_cyclic_linked_list(5)
    print(detect_cycle_point(cyclic_head).data, "============================", cyclic_head.data)

main()
