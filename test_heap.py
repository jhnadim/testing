from heap import Heap
from stack import Stack


import unittest

class TestHeap(unittest.TestCase):
    
 def test_init(self):
    heap = Heap()
    self.assertIsInstance(heap, Heap)
    self.assertEqual(heap.heap, [])

 def test_push(self):
    heap = Heap()
    heap.push(5)
    self.assertEqual(heap.heap, [5])
    heap.push(3)
    self.assertEqual(heap.heap, [3, 5])
    heap.push(4)
    self.assertEqual(heap.heap, [3, 5, 4])
    heap.push(1)
    self.assertEqual(heap.heap, [1, 3, 4, 5])

 def test_pop(self):
    heap = Heap()
    with self.assertRaises(ValueError):
        heap.pop()
    heap.push(3)
    heap.push(1)
    heap.push(5)
    self.assertEqual(heap.pop(), 1)
    self.assertEqual(heap.pop(), 3)
    self.assertEqual(heap.pop(), 5)
    with self.assertRaises(ValueError):
        heap.pop()

 def test_peek(self):
    heap = Heap()
    with self.assertRaises(ValueError):
        heap.peek()
    heap.push(3)
    self.assertEqual(heap.peek(), 3)
    heap.push(1)
    self.assertEqual(heap.peek(), 1)
    heap.push(5)
    self.assertEqual(heap.peek(), 1)

 def test_is_empty(self):
    heap = Heap()
    self.assertTrue(heap.is_empty())
    heap.push(3)
    self.assertFalse(heap.is_empty())
    heap.pop()
    self.assertTrue(heap.is_empty())

 def test_push_pop_peek(self):
    heap = Heap()
    heap.push(3)
    heap.push(1)
    heap.push(5)
    self.assertEqual(heap.pop(), 1)
    self.assertEqual(heap.peek(), 3)
    heap.push(4)
    self.assertEqual(heap.peek(), 3)
    heap.push(2)
    self.assertEqual(heap.pop(), 2)
    self.assertEqual(heap.pop(), 3)
    self.assertEqual(heap.pop(), 4)
    self.assertEqual(heap.pop(), 5)

 def test_push_all_equal(self):
    heap = Heap()
    heap.push(3)
    heap.push(3)
    heap.push(3)
    self.assertEqual(heap.pop(), 3)
    self.assertEqual(heap.pop(), 3)
    self.assertEqual(heap.pop(), 3)

 def test_push_one_value(self):
    heap = Heap()
    heap.push(3)
    self.assertEqual(heap.pop(), 3)

 def test_push_empty(self):
    heap = Heap()
    heap.push(3)
    self.assertFalse(heap.is_empty())

 def test_push_pop(self):
    heap = Heap()
    heap.push(3)
    heap.push(1)
    heap.push(5)
    heap.push(4)
    heap.push(2)
    self.assertEqual(heap.pop(), 1)
    self.assertEqual(heap.pop(), 2)
    self.assertEqual(heap.pop(), 3)
    self.assertEqual(heap.pop(), 4)
    self.assertEqual(heap.pop(), 5)

 def test_pop_empty(self):
    heap = Heap()
    with self.assertRaises(ValueError):
        heap.pop()

 def test_peek_empty(self):
    heap = Heap()
    with self.assertRaises(ValueError):
        heap.peek()

 def test_pop_one_value(self):
    heap = Heap()
    heap.push(3)
    self.assertEqual(heap.pop(), 3)
    self.assertTrue(heap.is_empty())

 def test_peek_one_value(self):
    heap = Heap()
    heap.push(3)
    self.assertEqual(heap.peek(), 3)
    self.assertFalse(heap.is_empty())

 def test_is_empty_one_value(self):
    heap = Heap()
    heap.push(3)
    heap.pop()
    self.assertTrue(heap.is_empty())


if __name__ == '__main__':
    unittest.main()
