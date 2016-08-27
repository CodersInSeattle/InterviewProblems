class BinaryTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '{%d: (%r, %r)}' % (self.val, self.left, self.right)


def get_left_neighbors(array_of_nums):
    stack = []
    result = []
    for num in array_of_nums:
        while stack and num < stack[-1]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(None)
        stack.append(num)
    return result


def get_right_neighbors(array_of_nums):
    stack = []
    result = []
    for num in reversed(array_of_nums):
        while stack and num < stack[-1]:
            stack.pop()
        if stack:
            result.append(stack[-1])
        else:
            result.append(None)
        stack.append(num)
    return result[::-1]


def build_cartesian_tree(array_of_nums):
    nodes = {num: BinaryTreeNode(num) for num in array_of_nums}
    left_neighbors = get_left_neighbors(array_of_nums)
    right_neighbors = get_right_neighbors(array_of_nums)
    root = None
    for num, l_nei, r_nei in zip(array_of_nums, left_neighbors, right_neighbors):
        if l_nei is None and r_nei is None:
            root = nodes[num]
        elif l_nei < r_nei:
            nodes[r_nei].left = nodes[num]
        else:
            nodes[l_nei].right = nodes[num]
    return root


nums = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
print(get_left_neighbors(nums))
print(get_right_neighbors(nums))
print(build_cartesian_tree(nums))
