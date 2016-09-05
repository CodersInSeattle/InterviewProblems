def min_scalar_product(nums1, nums2):
    nums1_increasing = sorted(nums1)
    nums2_decreasing = sorted(nums2, reverse=True)
    return scalar_product(nums1_increasing, nums2_decreasing)


def scalar_product(nums1, nums2):
    return sum(x * y for x, y in zip(nums1, nums2))
