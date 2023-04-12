import unittest
from binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.bs = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_found_element(self):
        self.assertEqual(self.bs.search(3), 2)
        
    def test_not_found_element(self):
        self.assertEqual(self.bs.search(0), -1)
        
        
    def test_found_element_2(self):
        self.assertEqual(self.bs.search(8), 7)
        

    def test_not_found_element_2(self):
        self.assertEqual(self.bs.search(11), -1)
        
    def test_found_element_3(self):
        self.assertEqual(self.bs.search(10), 9)

    def test_not_found_element_3(self):
        self.assertEqual(self.bs.search(100), -1)
        

    def test_empty_list(self):
        bs_empty = BinarySearch([])
        self.assertEqual(bs_empty.search(1), -1)
        

    def test_single_element_list(self):
        bs_single = BinarySearch([5])
        self.assertEqual(bs_single.search(5), 0)
        self.assertEqual(bs_single.search(10), -1)

    def test_even_number_of_elements(self):
        bs_even = BinarySearch([1, 2, 3, 4, 5, 6])
        self.assertEqual(bs_even.search(3), 2)
        self.assertEqual(bs_even.search(6), 5)

    def test_odd_number_of_elements(self):
        bs_odd = BinarySearch([1, 2, 3, 4, 5])
        self.assertEqual(bs_odd.search(3), 2)
        self.assertEqual(bs_odd.search(5), 4)

    def test_repeated_elements(self):
        bs_repeated = BinarySearch([1, 2, 2, 3, 4, 4, 4, 5])
        self.assertEqual(bs_repeated.search(2), 1)
        self.assertEqual(bs_repeated.search(4), 5)

    def test_float_elements(self):
        bs_float = BinarySearch([1.0, 2.2, 3.3, 4.5, 5.6])
        self.assertEqual(bs_float.search(2.2), 1)
        self.assertEqual(bs_float.search(5.6), 4)

    def test_string_elements(self):
        bs_string = BinarySearch(['apple', 'banana', 'cherry', 'date', 'elderberry'])
        self.assertEqual(bs_string.search('cherry'), 2)
   

    def test_string_elements_2(self):
        bs_string = BinarySearch(['apple', 'banana', 'cherry', 'date', 'elderberry'])
        self.assertEqual(bs_string.search('elderberry'), 4)


    def test_mixed_type_elements(self):
        bs_mixed = BinarySearch([1, 2.5, 'apple', True, None])
        self.assertEqual(bs_mixed.search('apple'), 2)
       

if __name__ == '__main__':
    unittest.main()
