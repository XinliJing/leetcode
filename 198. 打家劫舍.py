class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return max(nums)
        # t = [0 for i in range(len(nums))]
        t = []
        t.append(nums[0])
        t.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            t.append(max(t[i-1], t[i-2]+nums[i]))
        return t[len(nums)-1]
        # 膜大佬
        # pre=cur=0
        # for i in nums:
        #     cur,pre=max(pre+i,cur),cur
        # return cur
