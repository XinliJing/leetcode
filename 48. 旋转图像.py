class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 先用reverse原地上下翻转，再进行转置
        n = len(matrix)
        times = int(n*n/2)
        matrix.reverse()
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 大佬的算法，我之前也有想到QAQ
#         length = len(matrix) - 1

#         def rotation(matrix, p, y):
#             # 每次旋转外围一圈，p作为起始点，依次为(0, 0), (1, 1), (2, 2)... 
#             # y作为外圈的另一个点，在p的对角上
#             # 每次旋转4个点（值交换）
#             if p[1] < y:

#                 matrix[p[0]][p[1]], matrix[p[1]][y], matrix[y][length-p[1]], matrix[length-p[1]][p[0]] = (
#                     matrix[length-p[1]][p[0]], matrix[p[0]][p[1]], matrix[p[1]][y], matrix[y][length-p[1]]
#                 )

#                 rotation(matrix, [p[0], p[1]+1], y)

#         for i in range(len(matrix) // 2):  # 后部分已经算过
#             rotation(matrix, [i, i], length - i)
