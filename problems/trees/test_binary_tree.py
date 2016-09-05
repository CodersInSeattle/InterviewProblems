import unittest

from Problems.trees import binary_tree


THREE = binary_tree.BinaryTreeNode(3)
TWO = binary_tree.BinaryTreeNode(2)
FIVE = binary_tree.BinaryTreeNode(5)
SEVEN = binary_tree.BinaryTreeNode(7)
SIX = binary_tree.BinaryTreeNode(6)
TEN = binary_tree.BinaryTreeNode(10)
TWO.left = SEVEN
TWO.right = SIX
FIVE.right = TEN
THREE.left = TWO
THREE.right = FIVE


class BinaryTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = binary_tree.BinaryTree(THREE)

    def test_is_balanced(self):
        self.assertTrue(self.tree.is_balanced())

    def test_lowest_common_ancestor_root(self):
        lca = self.tree.lowest_common_ancestor(THREE, TEN)
        self.assertEqual(lca, THREE)

    def test_lowest_common_ancestor_different_side(self):
        lca = self.tree.lowest_common_ancestor(SEVEN, TEN)
        self.assertEqual(lca, THREE)

    def test_lowest_common_ancestor_same_side(self):
        lca = self.tree.lowest_common_ancestor(TWO, SIX)
        self.assertEqual(lca, TWO)

    def test_is_bst(self):
        self.assertFalse(self.tree.is_bst())

    def test_contains_subtree_exists(self):
        self.assertTrue(self.tree.contains_subtree(FIVE))

    def test_contains_subtree_wrong_children(self):
        some_node = binary_tree.BinaryTreeNode('2')
        self.assertFalse(self.tree.contains_subtree(some_node))

    def test_paths_with_sum(self):
        paths_sum_up_to_12 = self.tree.paths_with_sum(12)
        self.assertEqual([[SEVEN, TWO, THREE]], paths_sum_up_to_12)


if __name__ == '__main__':
    unittest.main()
