"""
Given an unsorted array nums, reorder it such that
  nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.
"""


def wiggle_sort_ii(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    nums_sorted = sorted(nums)
    nums_len = len(nums)
    left, right = (nums_len-1)/2, nums_len-1
    for i in xrange(nums_len):
        if i % 2 == 0:
            nums[i] = nums_sorted[left]
            left -= 1
        else:
            nums[i] = nums_sorted[right]
            right -= 1


