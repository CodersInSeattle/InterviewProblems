"""
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.
"""


def sort_colors(nums):
    zero_idx = one_idx = 0
    two_idx = len(nums) - 1
    while one_idx <= two_idx:
        if nums[one_idx] == 1:
            one_idx += 1
        elif nums[one_idx] == 0:
            nums[zero_idx], nums[one_idx] = nums[one_idx], nums[zero_idx]
            zero_idx += 1
            one_idx += 1
        else:
            nums[one_idx], nums[two_idx] = nums[two_idx], nums[one_idx]
            two_idx -= 1
