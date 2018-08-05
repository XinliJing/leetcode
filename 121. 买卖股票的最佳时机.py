class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        t = []
        for i in range(len(prices)-1):
            t.append(prices[i+1] - prices[i])
        thisSum = 0
        maxSum = 0
        for i in range(len(t)):
            thisSum += t[i]
            if thisSum > maxSum:
                maxSum = thisSum
            elif thisSum < 0:
                thisSum = 0
        return maxSum
