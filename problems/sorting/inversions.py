def count_inversions(nums):
    if not nums:
        return ([], 0)
    if len(nums) == 1:
        return (nums, 0)
    half_size = len(nums) / 2
    left_subarray, right_subarray = nums[:half_size], nums[half_size:]
    left_sorted, left_inversions = count_inversions(left_subarray)
    right_sorted, right_inversions = count_inversions(right_subarray)
    i = j = 0
    total_sorted = []
    total_inversions = left_inversions + right_inversions
    while i < len(left_subarray) and j < len(right_subarray):
        if left_sorted[i] < right_sorted[j]:
            total_sorted.append(left_sorted[i])
            i += 1
        elif left_sorted[i] > right_sorted[j]:
            total_sorted.append(right_sorted[j])
            total_inversions += len(left_subarray) - i
            j += 1
        else:
            total_sorted.append(left_sorted[i])
            total_sorted.append(right_sorted[j])
            i += 1
            j += 1
    while i < len(left_subarray):
        total_sorted.append(left_sorted[i])
        i += 1
    while j < len(right_subarray):
        total_sorted.append(right_sorted[j])
        j += 1
    return (total_sorted, total_inversions)


if __name__ == '__main__':
    INTS = [3, 2, 4, 0, 5]
    print count_inversions(INTS)
