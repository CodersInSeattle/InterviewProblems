import random


class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '{%d: (%r, %r)}' % (self.val, self.left, self.right)

    def __eq__(self, another_node):
        return (self.val == another_node.val and
                self.left == another_node.left and
                self.right == another_node.right)

    def __ne__(self, another_node):
        return not self == another_node

    def lowest_common_ancestor(self, node1, node2):
        if self is node1 or self is node2:
            return self
        left_result = (self.left.lowest_common_ancestor(node1, node2)
                       if self.left else None)
        right_result = (self.right.lowest_common_ancestor(node1, node2)
                        if self.right else None)
        if left_result and right_result:
            return self
        else:
            return left_result or right_result

    def paths_with_sum(self, target):
        if not self.left and not self.right:
            return [[self]] if self.val == target else []
        paths_from_left, paths_from_right = [], []
        if self.left:
            paths_from_left = self.left.paths_with_sum(target - self.val)
            for left_path in paths_from_left:
                left_path.append(self)
        if self.right:
            paths_from_right = self.right.paths_with_sum(target - self.val)
            for right_path in paths_from_right:
                right_path.append(self)
        return paths_from_left + paths_from_right

    def contains_subtree(self, node):
        if self == node:
            return True
        try:
            return (self.left.contains_subtree(node) or
                    self.right.contains_subtree(node))
        except AttributeError:
            return False

    def _is_balanced_and_height(self):
        left_balanced, left_height = (self.left._is_balanced_and_height()
                                      if self.left else (True, -1))
        right_balanced, right_height = (self.right._is_balanced_and_height()
                                        if self.right else (True, -1))
        total_balanced = (abs(left_height - right_height) <= 1 and
                          left_balanced and right_balanced)
        total_height = max(left_height, right_height) + 1
        return (total_balanced, total_height)

    def _is_in_range(self, low, high):
        try:
            return (self.val < high and self.val > low and
                    self.left._is_in_range(low, self.val) and
                    self.right._is_in_range(self.val, high))
        except AttributeError:
            return True


class BinaryTree(object):
    def __init__(self, root):
        self.root = root
        self._stack = [root]

    def __repr__(self):
        return 'Binary Tree rooted at %r' % self.root

    def __eq__(self, another_tree):
        return self.root == another_tree.root

    def __ne__(self, another_tree):
        return not self == another_tree

    def __iter__(self):
        return self

    def next(self):
        if self._stack:
            current = self._stack.pop()
            if current.left:
                self._stack.append(current.left)
            if current.right:
                self._stack.append(current.right)
            return current
        else:
            raise StopIteration()

    def is_balanced(self):
        return self.root._is_balanced_and_height()[0]

    def is_bst(self):
        return self.root._is_in_range(float('-inf'), float('inf'))

    def lowest_common_ancestor(self, node1, node2):
        return self.root.lowest_common_ancestor(node1, node2)

    def contains_subtree(self, node):
        return self.root.contains_subtree(node)

    def paths_with_sum(self, target):
        return self.root.paths_with_sum(target)

    def random_node(self):
        count = 0
        while True:
            try:
                current_node = self.next()
                count += 1
                if self._should_update(count):
                    result = current_node
            except StopIteration:
                break
        return result

    @staticmethod
    def _should_update(n):
        random_int = random.randint(1, n)
        return random_int == 1
