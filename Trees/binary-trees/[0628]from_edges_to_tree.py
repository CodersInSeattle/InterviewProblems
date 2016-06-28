"""
Example:
Given a list of edges:
    [('being', 'plant'),
     ('plant', 'flower'),
     ('animal', 'bird'),
     ('being', 'animal'),
     ('fish', 'salmon'),
     ('animal', 'human'),
     ('animal', 'fish')]

These edges represent the following tree:

                           being
                         /       \
                        /         \
                       /           \
                    plant          animal
                    /             /   |   \
                   /             /    |    \
                 flower       bird  human  fish
                                            |
                                          salmon
"""

from collections import defaultdict
from collections import deque


class FindRoot(object):
    def __init__(self, list_of_edges):
        self.list_of_edges = list_of_edges

    def find_root_using_dict(self):
        is_child = defaultdict(bool)
        for parent, child in self.list_of_edges:
            is_child[parent] = is_child[parent]
            is_child[child] = True
        for node, is_a_child in is_child.iteritems():
            if not is_a_child:
                return node

    def find_root_using_set(self):
        parents, children = set(), set()
        for parent, child in self.list_of_edges:
            parents.add(parent)
            children.add(child)
        roots = parents - children
        return roots.pop()


class FindLeaves(object):
    def __init__(self, list_of_edges):
        self.list_of_edges = list_of_edges

    def find_leaves_using_dict(self):
        is_parent = defaultdict(bool)
        for parent, child in self.list_of_edges:
            is_parent[parent] = True
            is_parent[child] = is_parent[child]
        leaves = {node for node, is_a_parent in is_parent.iteritems()
                  if not is_a_parent}
        return leaves

    def find_leaves_using_set(self):
        parents, children = set(), set()
        for parent, child in self.list_of_edges:
            parents.add(parent)
            children.add(child)
        leaves = children - parents
        return leaves


class TreePrinter(object):
    def __init__(self, list_of_edges):
        self.nodes_to_children = _populate_children(list_of_edges)

    def find_root(self):
        candidates = set(self.nodes_to_children.keys())
        for children in self.nodes_to_children.itervalues():
            for child in children:
                candidates.discard(child)
        return candidates.pop()

    def print_dfs(self):
        root = self.find_root()
        stack = [(root, 0)]
        while stack:
            current_node, current_level = stack.pop()
            print '  ' * current_level + current_node
            for child in reversed(self.nodes_to_children[current_node]):
                stack.append((child, current_level + 1))

    def print_level_order_storing_level(self):
        root = self.find_root()
        queue = deque([(root, 0)])
        prev_level = -1
        nodes_in_current_level = []
        while queue:
            current_node, current_level = queue.popleft()
            if current_level > 0 and current_level != prev_level:
                _print_level(nodes_in_current_level)
                nodes_in_current_level = []
                prev_level = current_level
            nodes_in_current_level.append(current_node)
            for child in self.nodes_to_children[current_node]:
                queue.append((child, current_level + 1))
        _print_level(nodes_in_current_level)

    def print_level_order(self):
        root = self.find_root()
        queue = deque([(root, 0)])
        prev_level = -1
        while queue:
            current_node, current_level = queue.popleft()
            if current_level > 0 and current_level != prev_level:
                print
                prev_level = current_level
            print current_node,
            for child in self.nodes_to_children[current_node]:
                queue.append((child, current_level + 1))

    def get_leaves(self, root):
        if not root:
            return []
        if not self.nodes_to_children[root]:
            return [root]
        leaves = []
        for child in self.nodes_to_children[root]:
            leaves.extend(self.get_leaves(child))
        return leaves


def _print_level(nodes_in_same_level):
    print ' '.join(nodes_in_same_level)


def _populate_children(list_of_edges):
    nodes = defaultdict(list)
    for parent, child in list_of_edges:
        nodes[parent].append(child)
    return nodes


if __name__ == '__main__':
    LIST_OF_EDGES = [('being', 'plant'),
                     ('plant', 'flower'),
                     ('animal', 'bird'),
                     ('being', 'animal'),
                     ('fish', 'salmon'),
                     ('animal', 'human'),
                     ('animal', 'fish')]
    LEAVES = ['flower', 'bird', 'human', 'salmon']

    FR = FindRoot(LIST_OF_EDGES)
    assert FR.find_root_using_dict() == 'being'
    assert FR.find_root_using_set() == 'being'

    FL = FindLeaves(LIST_OF_EDGES)
    assert FL.find_leaves_using_dict() == set(LEAVES)
    assert FL.find_leaves_using_set() == set(LEAVES)

    TP = TreePrinter(LIST_OF_EDGES)
    assert TP.get_leaves(TP.find_root()) == LEAVES
    print '**********depth-first traversal**********'
    TP.print_dfs()
    print '**********breadth-first traversal, NOT storing level**********'
    TP.print_level_order()
    print '**********breadth-first traversal, storing level**********'
    TP.print_level_order_storing_level()
