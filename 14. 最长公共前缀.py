class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        lenMin = 999
        string = ""
        for i in range(len(strs)):
            if len(strs[i]) < lenMin:
                lenMin = len(strs[i])
        for i in range(lenMin):
            flag = 1
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    flag = 0
                if flag == 0:
                    break
            if flag == 0:
                break
            else:
                string = string + strs[0][i]
        return string
