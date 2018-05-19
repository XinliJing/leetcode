class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:              #要注意list越界，特别是list为空的时候；
            return 0
        point = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[point]:
                point = point +1
                nums[point] = nums[i]
        return point+1
    
        #多多查看优秀代码。
        # nums[:] = sorted(set(nums))   set()得到的结果是无序不重复的元素集合
        # return len(nums)
        #nums[:] = sorted(list(set(nums)))
        #return len(set(nums))
