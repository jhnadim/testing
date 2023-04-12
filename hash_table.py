class HashTable:
    """
    A simple implementation of a hashtable data structure.
    Supports the following methods:

    - __init__(size): create a new hashtable with the given size.
    - __setitem__(key, value): add a new key-value pair to the hashtable.
    - __getitem__(key): retrieve the value associated with the given key.
    - __delitem__(key): remove the key-value pair associated with the given key.
    - __len__(): return the number of key-value pairs in the hashtable.
    """

    def __init__(self, size=1000):
        """
        Create a new hashtable with the given size.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        """
        Add a new key-value pair to the hashtable.
        """
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def __getitem__(self, key):
        """
        Retrieve the value associated with the given key.
        """
        index = self._hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        raise KeyError(f"Key '{key}' not found in hashtable")

    def __delitem__(self, key):
        """
        Remove the key-value pair associated with the given key.
        """
        index = self._hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found in hashtable")

    def __len__(self):
        """
        Return the number of key-value pairs in the hashtable.
        """
        count = 0
        for bucket in self.table:
            count += len(bucket)
        return count

    def _hash_function(self, key):
        """
        A simple hash function that returns an integer between 0 and self.size-1.
        """
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum([ord(c) for c in key]) % self.size
        else:
            return hash(key) % self.size
