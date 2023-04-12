import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    """
    Test cases for the Tree class.
    """

    def test_init(self):
        """
        Test creating a new Tree object.
        """
        tree = Tree(5)
        self.assertEqual(tree.value, 5)

    def test_add_child(self):
        """
        Test adding a child node to a Tree object.
        """
        tree = Tree(5)
        tree.add_child(3)
        self.assertEqual(tree.children[0].value, 3)

    def test_remove_child(self):
        """
        Test removing a child node from a Tree object.
        """
        tree = Tree(5)
        child = Tree(3)
        tree.children.append(child)
        tree.remove_child(child)
        self.assertEqual(len(tree.children), 0)

    def test_contains(self):
        """
        Test checking if a value is in a Tree object.
        """
        tree = Tree(5)
        tree.add_child(3)
        self.assertTrue(tree.contains(3))
        self.assertFalse(tree.contains(7))

    def test_size(self):
        """
        Test getting the size of a Tree object.
        """
        tree = Tree(5)
        tree.add_child(3)
        tree.add_child(7)
        tree.children[0].add_child(2)
        self.assertEqual(tree.size(), 4)

    def test_depth(self):
        """
        Test getting the depth of a Tree object.
        """
        tree = Tree(5)
        tree.add_child(3)
        tree.add_child(7)
        tree.children[0].add_child(2)
        tree.children[1].add_child(8)
        self.assertEqual(tree.depth(), 3)

    def test_init_invalid(self):
        """
        Test creating a new Tree object with an invalid value.
        """
        with self.assertRaises(TypeError):
            tree = Tree()

    def test_add_child_invalid(self):
        """
        Test adding a child node with an invalid value to a Tree object.
        """
        tree = Tree(5)
        with self.assertRaises(TypeError):
            tree.add_child()

    def test_remove_child_invalid(self):
        """
        Test removing an invalid child node from a Tree object.
        """
        tree = Tree(5)
        child = Tree(3)
        with self.assertRaises(ValueError):    # exception handeling
            tree.remove_child(child)

    def test_contains_invalid(self):
        """
        Test checking if an invalid value is in a Tree object.
        """
        tree = Tree(5)
        self.assertFalse(tree.contains(None))

    def test_size_invalid(self):
        """
        Test getting the size of an invalid Tree object.
        """
        tree = Tree(5)
        tree.children = None
        with self.assertRaises(TypeError):   # exception handeling
            tree.size()

    def test_depth_invalid(self):
        """
        Test getting the depth of an invalid Tree object.
        """
        tree = Tree(5)
        tree.children = None
        with self.assertRaises(TypeError):     # exception handeling
            tree.depth()

    def test_add_remove_child(self):
        """
        Test adding and removing a child node from a Tree object.
        """
        tree = Tree(5)
        tree.add_child(3)
        tree.add_child(7)
        tree.remove_child(tree.children[1])
        self.assertEqual(len(tree.children), 1)

    def test_contains_root(self):
        """
        Test checking if the root value is in a Tree object.
        """
        tree = Tree(5)
        self.assertTrue(tree.contains(5))

    def test_tree_remove_node(self):
    # Test removing a leaf node
     t = Tree(1)
     t.insert(2)
     t.insert(3)
     print(Tree(3))


    def test_tree_remove_node_2(self):
    # Test removing a node with two children
     t = Tree(4)
     t.insert(2)
     t.insert(6)
     t.insert(1)
     t.insert(3)
     t.insert(5)
     t.insert(7)
     print(Tree(5))




if __name__ == '__main__':
    unittest.main()

