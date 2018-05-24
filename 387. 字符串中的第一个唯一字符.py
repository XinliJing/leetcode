class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # listS = list(s)
        # judge = []
        # for i in range(len(listS)):
        #     judge = s[0:i] + s[i+1:]
        #     if s[i] not in judge:
        #         return i
        # return -1

        lowercase = string.ascii_lowercase   # string.ascii_lowercase返回小写字母
        L_index = [s.index(label) for label in lowercase if s.count(label) == 1]    # s.count(label) 返回label字符串在s字符串中出现的次数
        return min(L_index) if  len(L_index) else -1
