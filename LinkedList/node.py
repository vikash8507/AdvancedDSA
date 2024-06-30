from typing import Any

class Node:
    def __init__(self, data, next = None) -> None:
        self.data: Any = data
        self.next: Node | None = next
