class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 方法一：      感觉代码也不少诶
        for i in range(9):
            temp1 = []
            temp2 = []
            temp3 = []
            for j in range(9):
                row = int(j/3) + int(i/3)*3
                col = j%3+i%3*3
                num1 = board[i][j]
                num2 = board[j][i]
                num3 = board[row][col]
                if num1 != '.' and num1 in temp1:
                    return False
                if num2 != '.' and num2 in temp2:
                    return False
                if num3 != '.' and num3 in temp3:
                    return False
                if num1 not in temp1:
                    temp1.append(num1)
                if num2 not in temp2:
                    temp2.append(num2)
                if num3 not in temp3:
                    temp3.append(num3)
        return True
    
#         方法二：
#         flag = 1
#         for i in range(9):
#             temp = []
#             for j in range(9):
#                 num = board[i][j]
#                 if board[i][j] not in temp:
#                     temp.append(num)
#                 elif num == '.':
#                     continue
#                 else:
#                     flag = 0

#         for i in range(9):
#             temp = []
#             for j in range(9):
#                 num = board[j][i]
#                 if num not in temp:
#                     temp.append(num)
#                 elif num == '.':
#                     continue
#                 else:
#                     flag = 0

#         for i in range(9):
#             temp = []
#             for j in range(9):
#                 row = int(j/3) + int(i/3)*3
#                 col = j%3+i%3*3
#                 num = board[row][col]
#                 if num not in temp:
#                     temp.append(num)
#                 elif num =='.':
#                     continue
#                 else:
#                     flag = 0
#         if flag == 0:
#             return False
#         else:
#             return True
