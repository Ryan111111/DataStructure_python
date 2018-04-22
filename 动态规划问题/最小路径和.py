#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午2:10

class Solution:
    def minPathSum(self,matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        record = [[0 for j in range(n)] for i in range(m)]  #生成一个指定大小的0矩阵
        for i in range(m):
            for j in range(n):
                if j==0 and i==0:
                    record[i][j] = matrix[i][j]
                elif j>=1 and i>=1:
                    record[i][j] = min(record[i][j-1],record[i-1][j])+matrix[i][j]
                elif j>=1:
                    record[i][j] = record[i][j-1]+matrix[i][j]
                else:
                    record[i][j] = record[i-1][j] + matrix[i][j]
        print(record[m-1][n-1])



ss = Solution()
ss.minPathSum([[1,2,3],[4,5,6],[7,8,9]])
