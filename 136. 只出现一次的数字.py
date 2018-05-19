class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #异或运算的巧妙运用
        tmp = 0
        for i in range(len(nums)):
            tmp ^= nums[i]
        return tmp
