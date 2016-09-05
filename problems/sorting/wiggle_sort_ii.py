"""
Given an unsorted array nums, reorder it such that
  nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.
"""


from InterviewProblems.Problems.src.Sorting import select_k_th_smallest
from copy import deepcopy


def wiggle_sort_nlogn(nums):
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


def wiggle_sort_linear_time(nums):
    nums_partitioned = deepcopy(nums)
    median = select_k_th_smallest.select(nums_partitioned, len(nums)/2)
    nums_len = len(nums)
    left, right = (nums_len-1)/2, nums_len-1
    for i in xrange(nums_len):
        if i % 2 == 0:
            nums[i] = nums_partitioned[left]
            left -= 1
        else:
            nums[i] = nums_partitioned[right]
            right -= 1


A = [1,3,2,2,0,3]
wiggle_sort_linear_time(A)
print A
