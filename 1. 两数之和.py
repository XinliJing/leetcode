class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                
        # 大佬的
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] in d:
        #         return [d[nums[i]], i]
        #     else:
        #         d[target - nums[i]] = i
        
        # 和大佬的速度差了100倍QQ
        # 活用字典
