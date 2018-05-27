class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sNew = ""
        flag = 1
        flagg = 1
        for c in str:
            if flag == 1:
                if c == ' ':
                    continue
                if (c == '+') or (c == '-') or (c in string.digits):
                    flag = 0
                else:
                    return 0
            if flag == 0 and flagg == 0:
                if c not in string.digits:
                    break
            flagg = 0
            sNew += c
        try:
            istr = int(sNew)
        except:
            return 0
        if istr > 2**31-1:
            return 2**31-1
        elif istr < -2**31:
            return -2**31
        else:
            return istr
