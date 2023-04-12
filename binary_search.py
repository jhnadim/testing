class BinarySearch:
    """
    A class that implements binary search on a sorted list.

    Supports the following methods:

    - __init__(self, lst): create a new BinarySearch object with a given list.
    - search(self, val): search for a given value in the list.
    - recursive_search(self, val): search for a given value in the list recursively.
    - lower_bound(self, val): find the lower bound of a given value in the list.
    - upper_bound(self, val): find the upper bound of a given value in the list.
    """

    def __init__(self, lst):
        """
        Create a new BinarySearch object with a given list.

        :param lst: The list to search in.
        """
        self.lst = lst

    def search(self, val):
        """
        Search for a given value in the list using iterative binary search.

        :param val: The value to search for.
        :return: The index of the value if found, else -1.
        """
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lst[mid] == val:
                return mid
            elif self.lst[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    

    def recursive_search(self, val):
        """
        Search for a given value in the list using recursive binary search.

        :param val: The value to search for.
        :return: The index of the value if found, else -1.
        """
        def _recursive_search(left, right, val):
            if left > right:
                return -1
            mid = (left + right) // 2
            if self.lst[mid] == val:
                return mid
            elif self.lst[mid] < val:
                return _recursive_search(mid + 1, right, val)
            else:
                return _recursive_search(left, mid - 1, val)
        return _recursive_search(0, len(self.lst) - 1, val)

    def lower_bound(self, val):
        """
        Find the lower bound of a given value in the list.

        :param val: The value to find the lower bound for.
        :return: The index of the lower bound.
        """
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lst[mid] >= val:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def upper_bound(self, val):
        """
        Find the upper bound of a given value in the list.

        :param val: The value to find the upper bound for.
        :return: The index of the upper bound.
        """
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lst[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        return right
