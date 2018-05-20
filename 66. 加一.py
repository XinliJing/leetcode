class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
#         想太少QQ
#         digits[-1] += 1
#         return digits
        
#         列表太长转为整数尾数容易出错
#         data = 0
#         for x in digits:
#             data += x
#             data *= 10
#         data /= 10
#         data += 1
        
#         res = []
#         for y in str(int(data)):
#             res.append(int(y))
#         return res

#         if len(str(digits[-1]+1)) == len(str(digits[-1])):
#             digits[-1] += 1
#             return digits
#         else:
#             for i in range(len(str(digits[-1]))):
#                 digits.pop()
#             digits.append(1)
#             for i in range(len(str(digits[-1]))):
#                 digits.append(0)
#             return digits

        # 脑壳痛……每个元素的范围是[0,9)而不是[0,+∞)，就很郁闷
        # 掌握了insert()方法的使用，以及range的倒序
        a = 1  
        for i in range(len(digits)-1, -1, -1):  
            digits[i] += a  
            a = 0  
            if digits[i]>=10:  
                a = 1  
                digits[i] = 0  
            elif i > 0:  
                return digits  
        if a == 1:  
            digits.insert(0, 1)  
        return digits  
