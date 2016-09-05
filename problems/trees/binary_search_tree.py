from Problems.trees import binary_tree


class BinarySearchTreeNode(binary_tree.BinaryTreeNode):
    def __init__(self, val):
        super(BinarySearchTreeNode, self).__init__(val)

    def get_leftmost(self):
        current = self
        while current.left:
            current = current.left
        return current

    def get_rightmost(self):
        current = self
        while current.right:
            current = current.right
        return current

    def lowest_common_ancestor(self, small, big):
        if small.val <= self.val <= big.val:
            return self
        elif self.val > big.val and self.left:
            return self.left.lowest_common_ancestor(small, big)
        elif self.val < big.val and self.right:
            return self.right.lowest_common_ancestor(small, big)
        else:
            return None

    def search_closest(self, target):
        if self.right and self.val < target:
            right_closest = self.right.search_closest(target)
            if abs(right_closest - target) < abs(self.val - target):
                return right_closest
        elif self.left and self.val > target:
            left_closest = self.left.search_closest(target)
            if abs(left_closest - target) < abs(self.val - target):
                return left_closest
        return self.val

    def get_succ(self, node):
        if node.right:
            return self.right.get_leftmost()
        root = self
        succ = None
        while root:
            if node.val < root.val:
                succ = root
                root = root.left
            elif node.val > root.val:
                root = root.right
            else:
                return succ

    def get_pred(self, node):
        if node.left:
            return self.left.get_rightmost()
        root = self
        pred = None
        while root:
            if node.val > root.val:
                pred = root
                root = root.right
            elif node.val < root.val:
                root = root.right
            else:
                return pred

    def split_tree(self, threshold):
        if self.val == threshold:
            right_subtree = self.right
            self.right = None
            return (self, right_subtree)
        elif self.val > threshold and self.left:
            left_res, self.left = self.left.split_tree(threshold)
            return (left_res, self)
        elif self.val < threshold and self.right:
            self.right, right_res = self.right.split_tree(threshold)
            return (self, right_res)
        else:
            return (None, None)

    def smallest_node_at_least(self, threshold):
        if threshold == self.val:
            return self
        elif threshold < self.val:
            if self.left and threshold <= self.left.val:
                return self.left.smallest_node_at_least(threshold)
            else:
                return self
        else:
            if self.right:
                return self.right.smallest_node_at_least(threshold)
            else:
                return None


class BinarySearchTree(binary_tree.BinaryTree):
    def __init__(self, root):
        super(BinarySearchTree, self).__init__(root)

    def search_closest(self, target):
        return self.root.search_closest(target)

    def get_succ(self, node):
        return self.root.get_succ(node)

    def get_pred(self, node):
        return self.root.get_pred(node)

    def get_min_node(self):
        return self.root.get_leftmost()

    def get_max_node(self):
        return self.root.get_rightmost()

    def nodes_in_range(self, low, high):
        current = self.root.smallest_node_at_least(low)
        result = []
        while current.val <= high:
            result.append(current)
            current = current.get_succ()
        return result

    def lowest_common_ancestor(self, node1, node2):
        if node1.val > node2.val:
            node1, node2 = node2, node1
        return self.root.lowest_common_ancestor(node1, node2)

    def split_tree(self, threshold):
        return self.root.split_tree(threshold)
