import unittest

from InterviewProblems.problems.trees import from_edges_to_tree


LIST_OF_EDGES = [('being', 'plant'),
                 ('plant', 'flower'),
                 ('animal', 'bird'),
                 ('being', 'animal'),
                 ('fish', 'salmon'),
                 ('animal', 'human'),
                 ('animal', 'fish')]
ROOT = 'being'
LEAVES = ['flower', 'bird', 'human', 'salmon']


class FindRootTestCase(unittest.TestCase):
    def setUp(self):
        self.fr = from_edges_to_tree.FindRoot(LIST_OF_EDGES)

    def test_find_root_using_dict(self):
        self.assertEqual(self.fr.find_root_using_dict(), ROOT)

    def test_find_root_using_sets(self):
        self.assertEqual(self.fr.find_root_using_sets(), ROOT)


class FindLeavesTestCase(unittest.TestCase):
    def setUp(self):
        self.fl = from_edges_to_tree.FindLeaves(LIST_OF_EDGES)

    def test_find_leaves_using_dict(self):
        self.assertEqual(self.fl.find_leaves_using_dict(), set(LEAVES))

    def test_find_leaves_using_sets(self):
        self.assertEqual(self.fl.find_leaves_using_sets(), set(LEAVES))


class TreePrinterTestCase(unittest.TestCase):
    def setUp(self):
        self.tp = from_edges_to_tree.TreePrinter(LIST_OF_EDGES)

    def test_find_root(self):
        self.assertEqual(self.tp.find_root(), ROOT)

    def test_get_leaves(self):
        self.assertEqual(self.tp.get_leaves(ROOT), LEAVES)


if __name__ == '__main__':
    unittest.main()
