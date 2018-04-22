#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/19 下午1:39

class Solution:
    def minPathSum(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        record = [[0 for j in range(n)]for i in range(m)]  #创建一个m*n的0矩阵

        for i in range(m):
            for j in range(n):
                if j == 0 and i == 0:
                    record[i][j] = matrix[i][j]
                elif j>=1 and i>=1:
                    record[i][j] = min(record[i-1][j],record[i][j-1])+matrix[i][j]
                elif j>=1:
                    record[i][j] = record[i][j-1] + matrix[i][j]
                elif i>=1:
                    record[i][j] = record[i-1][j] + matrix[i][j]
        return record[m-1][n-1]