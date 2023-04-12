import unittest


from test_tennis_kata import MyTestCase
from test_stack import TestStack
from test_heap import TestHeap
from test_hashtable import TestHashTable
from test_deque import TestDeque
from test_tree import TestTree
from test_calculator import TestCalculator
from test_trigonometry import TestTrigonometry
from test_sorting import TestSorting
from test_binary_search import TestBinarySearch

# create a test suite combining all the imported test cases
test_suite = unittest.TestSuite()

test_suite.addTest(unittest.makeSuite(MyTestCase))
test_suite.addTest(unittest.makeSuite(TestStack))
test_suite.addTest(unittest.makeSuite(TestHeap))
test_suite.addTest(unittest.makeSuite(TestHashTable))
test_suite.addTest(unittest.makeSuite(TestDeque))
test_suite.addTest(unittest.makeSuite(TestTree))
test_suite.addTest(unittest.makeSuite(TestCalculator))
test_suite.addTest(unittest.makeSuite(TestTrigonometry))
test_suite.addTest(unittest.makeSuite(TestSorting))
test_suite.addTest(unittest.makeSuite(TestBinarySearch))

# run the test suite
unittest.TextTestRunner().run(test_suite)
