class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        thisSum = 0
        maxSum = nums[0]
        # if len(nums) == 1:
        #     return nums[0]
        for i in range(len(nums)):
            thisSum += nums[i]
            # maxSum = max(maxSum, thisSum)
            if thisSum > maxSum:
                maxSum = thisSum
            if thisSum < 0:
                thisSum = 0
        return maxSum
