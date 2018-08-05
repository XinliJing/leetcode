class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        t = [1, 1]
        for i in range(0, n-1):
            x = t[-1] + t[-2]
            t.append(x)
        return t[-1]
