#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午3:57

class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        record = [[0 for j in range(n)] for i in range(m)]
        # 对于第1行，第1列，当然元素是1的，以它为右下角的正方形边长就是1
        for j in range(n):
            if matrix[0][j] == 1:
                record[0][j] = 1
        for i in range(m):
            if matrix[i][0] == 1:
                record[i][0] = 1
        i = 1
        result = 0
        while i < m:
            j = 1
            while j < n:
                # 这个值是1，才有分析的必要，否则肯定是0
                if matrix[i][j] == 1:
                    record[i][j] = min(record[i - 1][j - 1], record[i - 1][j], record[i][j - 1]) + 1
                j += 1
            result = max(result, max(record[i]))
            i += 1
        # result计算的是边长，而需要返回的是面积
        return pow(result, 2)
        # write your code here