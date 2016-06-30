class BinaryTreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        pass

    def search(self, key):
        pass

    def remove(self, key):
        pass

    def lowest_common_ancestor(self, node1, node2):
        pass

    def is_balanced(self):
        pass

    def get_height(self, node):
        pass

    def is_bst(self):
        pass


class BinarySearchTreeNode(BinaryTreeNode):
    def __init__(self):
        super(BinarySearchTreeNode, self).__init__()

    def search(self, key):
        pass

    def remove(self, key):
        pass

    def get_succ(self, node):
        pass

    def get_pred(self, node):
        pass

    def nodes_in_range(self, low, high):
        pass

    def get_min(self):
        pass

    def get_max(self):
        pass

    def lowest_common_ancestor(self, node1, node2):
        pass

    def split_tree(self, threshold):
        pass
