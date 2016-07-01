class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = self._populate_height()

    def __repr__(self):
        return '{%r: (%r, %r)}' % (self.val, self.left, self.right)

    def search(self, key):
        stack = [self]
        while stack:
            current = stack.pop()
            if current.val == key:
                return current
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return None

    def lowest_common_ancestor(self, node1, node2):
        pass

    def is_balanced(self):
        if not self.left and not self.right:
            return True
        elif not self.left:
            return self.right.height <= 1 and self.right.is_balanced()
        elif not self.right:
            return self.left.height <= 1  and self.left.is_balanced()
        else:
            return (abs(self.left.height - self.right.height) <= 1 and
                    self.left.is_balanced() and self.right.is_balanced())

    def get_height(self, node):
        pass

    def is_bst(self):
        pass

    def contains_subtree(self, node):
        pass

    def random_node(self):
        pass

    def paths_with_sum(self, target):
        pass

    def _populate_height(self):
        left_height = self.left._populate_height() if self.left else -1
        right_height = self.right._populate_height() if self.right else -1
        self.height = max(left_height, right_height) + 1
        return self.height


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

