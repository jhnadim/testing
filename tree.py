class Tree:
    """
    A basic tree data structure.

    Supports the following methods:

    - __init__(value): create a new Tree with a given value as its root node.
    - add_child(value): add a new child node with the given value.
    - remove_child(child): remove a given child node.
    - contains(value): check if a given value is in the tree.
    - size(): return the number of nodes in the tree.
    - depth(): return the maximum depth of the tree.
    """

    def __init__(self, value):
        """
        Create a new Tree with a given value as its root node.
        """
        self.value = value
        self.children = []
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value):
        """
        Insert a new node with the given value into the tree.
        """
        if value < self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def find_node(self, value):
        """
        Return the node with the given value, or None if it does not exist.
        """
        if value == self.value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.find_node(value)
        elif value > self.value and self.right is not None:
            return self.right.find_node(value)
        else:
            return None

    def add_child(self, value):
        """
        Add a new child node with the given value.
        """
        child = Tree(value)
        self.children.append(child)

    def remove_child(self, child):
        """
        Remove a given child node.
        """
        if child in self.children:
            self.children.remove(child)
        else:
            raise ValueError("Child not found in tree")

    def contains(self, value):
        """
        Check if a given value is in the tree.
        """
        if self.value == value:
            return True
        else:
            for child in self.children:
                if child.contains(value):
                    return True
        return False

    def size(self):
        """
        Return the number of nodes in the tree.
        """
        count = 1
        for child in self.children:
            count += child.size()
        return count

    def depth(self):
        """
        Return the maximum depth of the tree.
        """
        if len(self.children) == 0:
            return 1
        else:
            max_depth = 0
            for child in self.children:
                child_depth = child.depth()
                if child_depth > max_depth:
                    max_depth = child_depth
            return max_depth + 1
