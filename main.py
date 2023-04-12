from stack import Stack
from tennis_kata import Player , announce_score
from heap import Heap
from hash_table import HashTable
from deque import Deque
from trigonometry import Trigonometry
from calculator import Calculator
from sorting import Sorting
from binary_search import BinarySearch


# Stack implementation
print("****************Stack********************")
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # prints 3
print(s.size())  # prints 3
s.pop()
print(s.peek())  # prints 2
print(s.is_empty())  # prints False
s.pop()
s.pop()
print(s.is_empty())  # prints True
print(" ")

print("***************Tennis******************")
# Define constant player names and scores
PLAYER_1_NAME = "Player 1"
PLAYER_2_NAME = "Player 2"
PLAYER_1_SCORE = 3
PLAYER_2_SCORE = 4

# Create two Player objects with constant names and scores
player_1 = Player(PLAYER_1_NAME, PLAYER_1_SCORE)
player_2 = Player(PLAYER_2_NAME, PLAYER_2_SCORE)

# Get the current game score
score = announce_score(player_1, player_2)

# Print the score
print(score)

print(" ")
print("****************Binary Stack***************")
# create a new heap
h = Heap()

# add some values to the heap
h.push(3)
h.push(1)
h.push(4)
h.push(1)
h.push(5)

# pop values off the heap and print them
while not h.is_empty():
    print(h.pop())
print(" ")


print("****************Hash Table*****************")

# Example usage of your hashtable class
table = HashTable()
table['apple'] = 5
table['banana'] = 7
table['orange'] = 3
print(table['banana'])  # Should print 7
del table['banana']
print(len(table))  # Should print 2
print(" ")


print("****************Deque*********************")
from deque import Deque

# create a new deque
d = Deque()

# add items to the back of the deque
d.append(1)
d.append(2)
d.append(3)

# add items to the front of the deque
d.appendleft(0)
d.appendleft(-1)

# remove and print items from the front of the deque
print(d.popleft())  # -1
print(d.popleft())  # 0

# remove and print items from the back of the deque
print(d.pop())  # 3
print(d.pop())  # 2
print(" ")

print("****************Calculator*****************")
f = Calculator()
result = f.add(3, 4)
print(f"The result of the 3+4 calculation is {result}")
print(" ")


print("****************Trigonometry*****************")
t = Trigonometry()
result = t.sin(0.5)
print(f"The sin of 0.5 radians is {result}")
print(" ")


print("****************Sorting*****************")
# Create a Sorting object with a list of integers
sorting = Sorting([5, 3, 8, 1, 2])

# Sort the list using bubble sort algorithm
sorting.bubble_sort()
print("Sorting list by Bubble sort")
print(sorting.lst)  # Output: [1, 2, 3, 5, 8]
print(" ")

print("****************Binary Search*****************")


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bs = BinarySearch(lst)

    # search for a value
    idx = bs.search(7)
    if idx == -1:
        print("Value not found.")
    else:
        print(f"Value found at index {idx}.")

    # find the lower bound of a value
    lb = bs.lower_bound(7)
    print(f"Lower bound of 7: {lb}.")

    # find the upper bound of a value
    ub = bs.upper_bound(7)
    print(f"Upper bound of 7: {ub}.")












