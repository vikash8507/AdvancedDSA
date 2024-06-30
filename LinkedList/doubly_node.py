
class DoublyNode:

    def __init__(self, data):
        self.data = data
        self.prev: DoublyNode | None = None
        self.next: DoublyNode | None = None
