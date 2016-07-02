import unittest

from InterviewProblems.Problems.src.Trees import binary_search_tree


SEVENTEEN = binary_search_tree.BinarySearchTreeNode(17)
SEVEN = binary_search_tree.BinarySearchTreeNode(7)
THIRTEEN = binary_search_tree.BinarySearchTreeNode(13)
TWENTYTHREE = binary_search_tree.BinarySearchTreeNode(23)
NINETEEN = binary_search_tree.BinarySearchTreeNode(19)
FORTYSEVEN = binary_search_tree.BinarySearchTreeNode(47)
TWENTYNINE = binary_search_tree.BinarySearchTreeNode(29)

SEVEN.right = THIRTEEN
TWENTYTHREE.left = NINETEEN
FORTYSEVEN.left = TWENTYNINE
TWENTYTHREE.right = FORTYSEVEN
SEVENTEEN.left = SEVEN
SEVENTEEN.right = TWENTYTHREE


class BinarySearchTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = binary_search_tree.BinarySearchTree(SEVENTEEN)

    def test_is_balanced(self):
        self.assertTrue(self.tree.is_balanced())

    def test_is_bst(self):
        self.assertTrue(self.tree.is_bst())

    def test_lowest_common_ancestor_root(self):
        lca = self.tree.lowest_common_ancestor(SEVENTEEN, THIRTEEN)
        self.assertEqual(lca, SEVENTEEN)

    def test_lowest_common_ancestor_different_side(self):
        lca = self.tree.lowest_common_ancestor(SEVEN, TWENTYNINE)
        self.assertEqual(lca, SEVENTEEN)

    def test_lowest_common_ancestor_same_side(self):
        lca = self.tree.lowest_common_ancestor(SEVEN, THIRTEEN)
        self.assertEqual(lca, SEVEN)

    # def test_contains_subtree_exists(self):
    #     self.assertTrue(self.tree.contains_subtree(FIVE))

    # def test_contains_subtree_wrong_children(self):
    #     some_node = binary_tree.BinaryTreeNode('2')
    #     self.assertFalse(self.tree.contains_subtree(some_node))

    # def test_paths_with_sum(self):
    #     paths_sum_up_to_12 = self.tree.paths_with_sum(12)
    #     self.assertEqual([[SEVEN, TWO, THREE]], paths_sum_up_to_12)


if __name__ == '__main__':
    unittest.main()
