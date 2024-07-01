from typing import Any

class StackWithList:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item) -> None:
        self.stack.append(item)
        self.top += 1

    def pop(self) -> None:
        if self.top == -1:
            return
        self.top -= 1
        return self.stack.pop()
    
    def peak(self) -> Any:
        return None if self.top == -1 else self.stack[self.top]

    def to_string(self) -> str:
        return "".join(self.stack)

    def generate_stack(self, items):
        for item in items:
            self.push(item)

    def print(self) -> None:
        for item in self.stack:
            print(item, end=" -> ")
        print()

    def is_empty(self) -> bool:
        return self.top == -1


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

class StackWithLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, item):
        new_item = Node(item)
        new_item.next = self.head
        self.head = new_item
    
    def pop(self) -> Any:
        if self.head is None:
            return
        poped = self.head
        self.head = self.head.next
        return poped.data
    
    def peak(self) -> Any:
        return self.head.data if self.head else None

    def to_string(self) -> str:
        tmp = self.head
        string = ""
        while tmp:
            string += str(tmp.data)
            tmp = tmp.next
        return string[-1::-1]

    def generate_stack(self, items):
        for item in items:
            self.push(item)

    def print(self) -> None:
        tmp = self.head
        while tmp:
            print(tmp.data, end=" -> ")
            tmp = tmp.next
        print()

    def is_empty(self) -> bool:
        return self.head is None
