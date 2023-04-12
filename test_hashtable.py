import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_setitem(self):
        # Test adding a key-value pair with a numeric key
        h = HashTable()
        h[123] = 'numeric_value'
        self.assertEqual(h[123], 'numeric_value')
        
    def test_setitem_1(self):
        # Test updating an existing key-value pair
        h = HashTable()
        h[123] = 'numeric_value'
        h['key'] = 'new_value'
        self.assertEqual(h['key'], 'new_value')
        
    def test_setitem_2(self):
        # Test adding a new key-value pair
        h = HashTable()
        h[123] = 'numeric_value'
        
        # Test adding a key-value pair with a numeric key
        h[123] = 'numeric_value'
        self.assertEqual(h[123], 'numeric_value')

    def test_getitem(self):
        # Test getting a value for an existing key
        h = HashTable()
        h['key'] = 'value'
        self.assertEqual(h['key'], 'value')

            
    def test_getitem_1(self):

        h = HashTable()

        # Test getting a value for a non-existing key
        with self.assertRaises(KeyError):
            h['non_existing_key']

    def test_delitem(self):
        # Test removing an existing key-value pair
        h = HashTable()
        h['key'] = 'value'
        del h['key']
        with self.assertRaises(KeyError):   # exception handeling
            h['key']


    def test_delitem_1(self):
        h = HashTable()

        # Test removing a non-existing key-value pair
        with self.assertRaises(KeyError):    # exception handeling
            del h['non_existing_key']

    def test_len(self):
        # Test the length of an empty hashtable
        h = HashTable()
        self.assertEqual(len(h), 0)


    def test_len_1(self):
        h = HashTable()
        # Test the length of a hashtable with one key-value pair
        h['key'] = 'value'
        self.assertEqual(len(h), 1)

        
    def test_len_2(self):
        # Test the length of an empty hashtable
        h = HashTable()

        # Test the length of a hashtable with multiple key-value pairs
        h['key1'] = 'value1'
        h['key2'] = 'value2'
        self.assertEqual(len(h), 2)
        

    def test_hash_function(self):
        # Test the hash function for an integer key
        h = HashTable()
        self.assertEqual(h._hash_function(123), 123 % h.size)


    def test_hash_function_1(self):
        # Test the hash function for an integer key
        h = HashTable()

        # Test the hash function for a string key
        self.assertEqual(h._hash_function('hello'), sum([ord(c) for c in 'hello']) % h.size)


        
    def test_hash_function_2(self):
        # Test the hash function for an integer key
        h = HashTable()
        # Test the hash function for a tuple key
        self.assertEqual(h._hash_function((1, 2, 3)), hash((1, 2, 3)) % h.size)
        
        
    def test_collision_resolution(self):
        # Test adding multiple key-value pairs to the same bucket
        h = HashTable()
        h['key1'] = 'value1'
        h['key2'] = 'value2'
        h['key3'] = 'value3'
        self.assertEqual(len(h.table[h._hash_function('key1')]), 1)


    def test_collision_resolution_1(self):
        # Test adding multiple key-value pairs to the same bucket
        h = HashTable()
        h['key1'] = 'value1'
        h['key2'] = 'value2'
        h['key3'] = 'value3'
        

        # Test updating a key-value pair in a bucket with multiple key-value pairs
        h['key1'] = 'new_value'
        self.assertEqual(len(h.table[h._hash_function('key1')]), 1)
        self.assertEqual(h['key1'], 'new_value')

    def test_collision_resolution_2(self):
        # Test adding multiple key-value pairs to the same bucket
        h = HashTable()
        h['key1'] = 'value1'
        h['key2'] = 'value2'
        h['key3'] = 'value3'
        
        # Test removing a key-value pair from a bucket with multiple key-value pairs
        del h['key1']
        self.assertEqual(len(h.table[h._hash_function('key1')]), 0)
        with self.assertRaises(KeyError):    # exception handeling
            h['key1']
            

if __name__ == '__main__':
    unittest.main()

