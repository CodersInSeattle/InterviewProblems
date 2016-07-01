import unittest

from ...src.Trees import bst


THREE = bst.BinaryTreeNode('3')
TWO = bst.BinaryTreeNode('2')
FIVE = bst.BinaryTreeNode('5')
SEVEN = bst.BinaryTreeNode('7')
SIX = bst.BinaryTreeNode('6')
TEN = bst.BinaryTreeNode('10')
TWO.left = SEVEN
TWO.right = SIX
FIVE.right = TEN
THREE.left = TWO
THREE.right = FIVE


class BinaryTreeNodeTestCase(unittest.TestCase):
    def setUp(self):
        self.root = THREE

    def test_search_root(self):
        found = self.root.search('3')
        self.assertEqual(found, THREE)

    def test_search_leaf(self):
        found = self.root.search('10')
        self.assertEqual(found, TEN)

    def test_search_mid(self):
        found = self.root.search('5')
        self.assertEqual(found, FIVE)

    def test_search_not_exist(self):
        found = self.root.search('8')
        self.assertEqual(found, None)

    def test_is_balanced(self):
        self.assertTrue(self.root.is_balanced())


if __name__ == '__main__':
    unittest.main()
