import unittest
from sorting import Sorting

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        # Test case with a random list
        s = Sorting([5, 3, 1, 4, 2])
        s.bubble_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])


    def test_bubble_sort_2(self):
        
        # Test case with an already sorted list
        s = Sorting([1, 2, 3, 4, 5])
        s.bubble_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])


    def test_bubble_sort_3(self):

        # Test case with a list in reverse order
        s = Sorting([5, 4, 3, 2, 1])
        s.bubble_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

    def test_selection_sort(self):
        # Test case with a random list
        s = Sorting([5, 3, 1, 4, 2])
        s.selection_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])



    def test_selection_sort_2(self):

        # Test case with an already sorted list
        s = Sorting([1, 2, 3, 4, 5])
        s.selection_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])


    def test_selection_sort_3(self):

        # Test case with a list in reverse order
        s = Sorting([5, 4, 3, 2, 1])
        s.selection_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        # Test case with a random list
        s = Sorting([5, 3, 1, 4, 2])
        s.insertion_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

        
    def test_insertion_sort_2(self):

        # Test case with an already sorted list
        s = Sorting([1, 2, 3, 4, 5])
        s.insertion_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

    def test_insertion_sort_3(self):

        # Test case with a list in reverse order
        s = Sorting([5, 4, 3, 2, 1])
        s.insertion_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

    def test_quick_sort(self):
        # Test case with a random list
        s = Sorting([5, 3, 1, 4, 2])
        s.quick_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])

        
    def test_quick_sort_2(self):

        # Test case with an already sorted list
        s = Sorting([1, 2, 3, 4, 5])
        s.quick_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])


    def test_quick_sort_3(self):

        # Test case with a list in reverse order
        s = Sorting([5, 4, 3, 2, 1])
        s.quick_sort()
        self.assertEqual(s.lst, [1, 2, 3, 4, 5])   
        
        
    def test_partition(self):

     # Test case with a list of equal elements
     s = Sorting([2, 2, 2, 2, 2])
     pivot_index = s.partition(0, 4)
     assert pivot_index == 4
     assert s.lst == [2, 2, 2, 2, 2]

    
    def test_partition_2(self):

     # Test case with a list of already sorted elements
     s = Sorting([1, 2, 3, 4, 5])
     pivot_index = s.partition(0, 4)
     assert pivot_index == 4
     assert s.lst == [1, 2, 3, 4, 5]
    
    def test_partition_3(self):

     # Test case with a list of reverse sorted elements
     s = Sorting([5, 4, 3, 2, 1])
     pivot_index = s.partition(0, 4)
     assert pivot_index == 0
     assert s.lst == [1, 4, 3, 2, 5]



if __name__ == '__main__':
    unittest.main()
