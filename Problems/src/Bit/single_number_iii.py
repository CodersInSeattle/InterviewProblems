import operator
import functools

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all = functools.reduce(operator.xor, nums)
        mask = all ^ (all & (all - 1))
        yes = no = 0
        for x in nums:
            if mask & x:
                yes ^= x
            else:
                no ^= x
        return [yes, no]


print Solution().singleNumber([1,2,1,2,3,4])
