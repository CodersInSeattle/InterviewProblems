"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and
an integer k.

Define a pair (u,v) which consists of one element from the first array and one
element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [[1,2],[1,4],[1,6]]

Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
Return: [[1,1],[1,1]]

Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3
Return: [[1,3],[2,3]]
"""

from heapq import heappush, heappop


def k_smallest_pairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    if not nums1 or not nums2:
        return []
    queue = [(nums1[0] + nums2[0], 0, 0)]
    result = []
    while queue and len(result) < k:
        _, i, j = heappop(queue)
        result.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heappush(queue, (nums1[i]+nums2[j+1], i, j+1))
        if j == 0 and i + 1 < len(nums1):
            heappush(queue, (nums1[i+1]+nums2[j], i+1, j))
    return result
