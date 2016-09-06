import operator
import functools


class Solution(object):

    @staticmethod
    def single_number(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all_xor = functools.reduce(operator.xor, nums)
        mask = all_xor ^ (all_xor & (all_xor - 1))
        yes = no = 0
        for x in nums:
            if mask & x:
                yes ^= x
            else:
                no ^= x
        return [yes, no]


print(Solution.single_number([1, 2, 1, 2, 3, 4]))
