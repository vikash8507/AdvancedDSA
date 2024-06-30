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

    def to_string(self):
        return "".join(self.stack)
