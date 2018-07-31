class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(n-1):
            nextString = ""
            count = 1
            for j in range(len(string)):
                # print(j)
                if j+1 < len(string) and string[j] == string[j+1]:
                    count += 1
                    continue
                else:
                    nextString = nextString + str(count) + string[j]
                    count = 1
                    # print(nextString)
            string = nextString
        return string
