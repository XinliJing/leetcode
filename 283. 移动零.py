class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        site = 0
        length = len(nums)
        i = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
                     
        # 1号大佬的代码
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] == 0:
        #         del nums[i]
        #         nums.append(0)
        
        # 2号大佬的代码
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[j], nums[i] = nums[i], nums[j]
        #         j += 1
        
        
        # 掌握python特有的交换方式
