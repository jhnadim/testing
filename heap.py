class Heap:
    """
    A binary heap data structure implemented as a list.
    The heap supports the following methods:

    - __init__(): create an empty heap.
    - push(val): add a new value to the heap.
    - pop(): remove and return the minimum value in the heap.
    - peek(): return the minimum value in the heap without removing it.
    - is_empty(): check if the heap is empty.
    """

    def __init__(self):
        """
        Create an empty heap.
        """
        self.heap = []

    def push(self, val):
        """
        Add a new value to the heap.
        """
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def pop(self):
        """
        Remove and return the minimum value in the heap.
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._percolate_down(0)
        return val

    def peek(self):
        """
        Return the minimum value in the heap without removing it.
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.heap[0]

    def is_empty(self):
        """
        Check if the heap is empty.
        """
        return len(self.heap) == 0

    def _percolate_up(self, index):
        """
        Move the value at the given index up the heap until it satisfies the heap property.
        """
        parent = (index - 1) // 2
        if parent < 0:
            return
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._percolate_up(parent)

    def _percolate_down(self, index):
        """
        Move the value at the given index down the heap until it satisfies the heap property.
        """
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        min_index = index
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[min_index]:
            min_index = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[min_index]:
            min_index = right_child
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._percolate_down(min_index)
