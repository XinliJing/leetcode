class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = ""
        for i in range(-1, -(len(s)+1), -1):
            l += s[i]
        return l
    
    
    
        # 最佳            灵活运用[::]
        # return s[::-1]
    
        # 次佳            join的用法
        # s = list(s)
        # s.reverse()
        # return ''.join(s)
