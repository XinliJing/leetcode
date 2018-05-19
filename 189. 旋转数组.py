class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # 对切片的灵活使用
        # print(nums[-3:])
        # print(nums[:-3])
        # print(nums[-3:]+nums[:-3])
        
        ans = nums[:]
        for i in range(len(nums)):
            ans[(i+k)%(len(nums))] = nums[i]
        for i in range(len(nums)):
            nums[i] = ans[i]
        
        # 最佳
        # length = len(nums)
        # i = k % length
        # nums[:] = nums[-i:]+nums[:-i]
