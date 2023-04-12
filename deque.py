class Deque:
    """
    A double-ended queue data structure, also known as a deque.

    Supports the following methods:

    - __init__(): create a new, empty deque.
    - append(item): add an item to the back of the deque.
    - appendleft(item): add an item to the front of the deque.
    - pop(): remove and return the item at the back of the deque.
    - popleft(): remove and return the item at the front of the deque.
    """

    def __init__(self):
        """
        Create a new, empty deque.
        """
        self.items = []

    def append(self, item):
        """
        Add an item to the back of the deque.
        """
        self.items.append(item)

    def appendleft(self, item):
        """
        Add an item to the front of the deque.
        """
        self.items.insert(0, item)

    def pop(self):
        """
        Remove and return the item at the back of the deque.
        """
        if len(self.items) == 0:
            raise IndexError("pop from an empty deque")
        return self.items.pop()

    def popleft(self):
        """
        Remove and return the item at the front of the deque.
        """
        if len(self.items) == 0:
            raise IndexError("pop from an empty deque")
        return self.items.pop(0)

def clear(self):
    """
    Remove all elements from the deque.
    """
    self.items = []



