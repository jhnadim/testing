from stack import Stack

import unittest

class TestStack(unittest.TestCase):
    def test_push(self):
        # Test push method with one item
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)

    def test_push_1(self):   
        # Test push method with multiple items
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)

    def test_push_2(self):
        # Test push method with empty stack
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
    

    def test_pop(self):
        # Test pop method with one item
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_pop_1(self):
        # Test pop method with multiple items
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)

    def test_pop_2(self):
        # Test pop method with empty stack
        stack = Stack()
        with self.assertRaises(Exception):    # exception handeling
            stack.pop()

    def test_peek(self):
        # Test peek method with one item
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
            
    def test_peek_1(self):
        # Test peek method with multiple items
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        
    def test_peek_2(self):
        # Test peek method with empty stack
        stack = Stack()
        with self.assertRaises(Exception):    # exception handeling
            stack.peek()
            
    def test_size(self):
        # Test size method with empty stack
        stack = Stack()
        self.assertEqual(stack.size(), 0)


    def test_size_1(self):
        # Test size method with one item
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.size(), 1)

    def test_size_2(self):
        # Test size method with multiple items
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 2)


    def test_is_empty(self):
        # Test is_empty method with empty stack
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_is_empty_1(self):

        # Test is_empty method with one item
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.is_empty())


    def test_is_empty_2(self):

        # Test is_empty method with multiple items
        stack = Stack()
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.is_empty())

    
if __name__ == '__main__':
    unittest.main()
    


        
