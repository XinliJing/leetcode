class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            num = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                else:
                    num = num + 1
                if num == len(needle):
                    return i
        return -1
