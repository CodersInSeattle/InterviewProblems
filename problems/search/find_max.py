def find_max_duplicate(nums, low, high):
    if high - low <= 1:  # length of nums at most 2
        return max(nums[low:high+1])
    mid = low + (high-low) / 2
    mid_left = mid - 1
    while mid_left >= low and nums[mid_left] == nums[mid]:
        mid_left -= 1
    if mid_left < low:
        return find_max_duplicate(nums, mid, high)
    elif nums[mid_left] > nums[mid]:
        return find_max_duplicate(nums, low, mid_left)
    else:
        return find_max_duplicate(nums, mid, high)


if __name__ == '__main__':
    assert find_max_duplicate([0, 0, 0, 0, 0], 0, 4) == 0
    assert find_max_duplicate([4, 4, 4, 6], 0, 3) == 6
    assert find_max_duplicate([2, 2, 2, 4, 4, 4, 3, 3, 1], 0, 8) == 4
    assert find_max_duplicate([4, 2, 2, 2, 1, 1, 1, 1, 0, 0], 0, 9) == 4
    assert find_max_duplicate([0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2], 0, 10) == 2
