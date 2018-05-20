class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # 我的算法
        # nums3 = []
        # for i in range(len(nums1)):
        #     if nums1[i] in nums3:
        #         continue
        #     else:
        #         temp = 0
        #         temp1 = 0
        #         temp2 = 0
        #         for j in range(len(nums1)):
        #             if nums1[j] == nums1[i]:
        #                 temp1 += 1
        #         for k in range(len(nums2)):
        #             if nums2[k] == nums1[i]:
        #                 temp2 += 1
        #         if temp1 > temp2:
        #             temp = temp2
        #         else:
        #             temp = temp1
        #         for m in range(temp):
        #             nums3.append(nums1[i])
        # return nums3
    
        # 大佬的算法
        res = []

        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in nums2:
            if i in dict1:
                #自己稍作修改，以一换二hhh
                if dict1[i] != 0:
                    res.append(i)
                    dict1[i] -= 1
                # if dict1[i] == 0:
                #     dict1.pop(i)
        return res
                    
