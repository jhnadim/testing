class Sorting:
    """
    A class that implements various sorting algorithms.

    Supports the following methods:

    - __init__(self, lst): create a new Sorting object with a given list.
    - bubble_sort(self): sort the list using the bubble sort algorithm.
    - selection_sort(self): sort the list using the selection sort algorithm.
    - insertion_sort(self): sort the list using the insertion sort algorithm.
    - quick_sort(self, start=0, end=None): sort the list using the quick sort algorithm.
    """

    def __init__(self, lst):
        """
        Create a new Sorting object with a given list.

        :param lst: The list to sort.
        """
        self.lst = lst

    def bubble_sort(self):
        """
        Sort the list using the bubble sort algorithm.
        """
        n = len(self.lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.lst[j] > self.lst[j+1]:
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]

    def selection_sort(self):
        """
        Sort the list using the selection sort algorithm.
        """
        n = len(self.lst)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.lst[j] < self.lst[min_idx]:
                    min_idx = j
            self.lst[i], self.lst[min_idx] = self.lst[min_idx], self.lst[i]

    def insertion_sort(self):
        """
        Sort the list using the insertion sort algorithm.
        """
        n = len(self.lst)
        for i in range(1, n):
            key = self.lst[i]
            j = i - 1
            while j >= 0 and key < self.lst[j]:
                self.lst[j+1] = self.lst[j]
                j -= 1
            self.lst[j+1] = key

    def quick_sort(self, start=0, end=None):
        """
        Sort the list using the quick sort algorithm.

        :param start: The starting index of the subarray to sort.
        :param end: The ending index of the subarray to sort.
        """
        if end is None:
            end = len(self.lst) - 1

        if start < end:
            pivot = self.partition(start, end)
            self.quick_sort(start, pivot-1)
            self.quick_sort(pivot+1, end)

    def partition(self, start, end):
        """
        Helper function for quick sort algorithm.

        :param start: The starting index of the subarray to partition.
        :param end: The ending index of the subarray to partition.
        :return: The index of the pivot element.
        """
        pivot = self.lst[end]
        i = start - 1
        for j in range(start, end):
            if self.lst[j] <= pivot:
                i += 1
                self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        self.lst[i+1], self.lst[end] = self.lst[end], self.lst[i+1]
        return i + 1
