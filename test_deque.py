import unittest
from deque import Deque

class TestDeque(unittest.TestCase):
    
        # Test append()
    def test_append(self):
        deque = Deque()
        deque.append(1)
        self.assertEqual(len(deque.items), 1)
        self.assertEqual(deque.items[0], 1)
        deque.append(2)
        self.assertEqual(len(deque.items), 2)
        self.assertEqual(deque.items[1], 2)
        deque.append(3)
        self.assertEqual(len(deque.items), 3)
        self.assertEqual(deque.items[2], 3)

    def test_init_empty_deque(self):
        # Test creating a new, empty deque
        d = Deque()
        self.assertEqual(len(d.items), 0)

    def test_append_single_item(self):
        # Test adding a single item to the back of the deque
        d = Deque()
        d.append(1)
        self.assertEqual(d.items, [1])

    def test_append_multiple_items(self):
        # Test adding multiple items to the back of the deque
        d = Deque()
        d.append(1)
        d.append(2)
        d.append(3)
        self.assertEqual(d.items, [1, 2, 3])

    def test_appendleft_single_item(self):
        # Test adding a single item to the front of the deque
        d = Deque()
        d.appendleft(1)
        self.assertEqual(d.items, [1])

    def test_appendleft_multiple_items(self):
        # Test adding multiple items to the front of the deque
        d = Deque()
        d.appendleft(1)
        d.appendleft(2)
        d.appendleft(3)
        self.assertEqual(d.items, [3, 2, 1])
        
            # Test pop()
    def test_pop(self):
        deque = Deque()
        deque.append(1)
        deque.append(2)
        deque.append(3)
        self.assertEqual(deque.pop(), 3)
        self.assertEqual(len(deque.items), 2)
        self.assertEqual(deque.pop(), 2)
        self.assertEqual(len(deque.items), 1)
        self.assertEqual(deque.pop(), 1)
        self.assertEqual(len(deque.items), 0)
        self.assertRaises(IndexError, deque.pop)

    def test_pop_single_item(self):
        # Test removing and returning a single item from the back of the deque
        d = Deque()
        d.append(1)
        self.assertEqual(d.pop(), 1)
        self.assertEqual(len(d.items), 0)

    def test_pop_multiple_items(self):
        # Test removing and returning multiple items from the back of the deque
        d = Deque()
        d.append(1)
        d.append(2)
        d.append(3)
        self.assertEqual(d.pop(), 3)
        self.assertEqual(d.pop(), 2)
        self.assertEqual(d.pop(), 1)
        with self.assertRaises(IndexError):   # Exception handling
            d.pop()

    def test_popleft_single_item(self):
        # Test removing and returning a single item from the front of the deque
        d = Deque()
        d.append(1)
        self.assertEqual(d.popleft(), 1)
        self.assertEqual(len(d.items), 0)

    def test_popleft_multiple_items(self):
        # Test removing and returning multiple items from the front of the deque
        d = Deque()
        d.append(1)
        d.append(2)
        d.append(3)
        self.assertEqual(d.popleft(), 1)
        self.assertEqual(d.popleft(), 2)
        self.assertEqual(d.popleft(), 3)
        with self.assertRaises(IndexError):      # exception handeling
            d.popleft()

    def test_pop_empty_deque(self):
        # Test removing an item from an empty deque
        d = Deque()
        with self.assertRaises(IndexError):  # exception handeling
            d.pop()

    def test_popleft_empty_deque(self):
        # Test removing an item from an empty deque
        d = Deque()
        with self.assertRaises(IndexError):   # exception handeling
            d.popleft()

    def test_clear_empty_deque(self):
        # Test clearing an empty deque
        d = Deque()
        
        self.assertEqual(len(d.items), 0)
        self.assertEqual(d.items, [])

    def test_clear_nonempty_deque(self):
        # Test clearing a non-empty deque
        d = Deque()
        d.append(1)
        d.append(2)
        d.append(3)
        self.assertEqual(len(d.items), 3)
       

if __name__ == '__main__':
    unittest.main()
