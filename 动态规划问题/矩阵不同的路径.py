#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/19 下午3:42

class Solution:
    def uniquePaths(self,m,n):
        if m<1 or n<1:
            return 0
        record = [[1 for j in range(n)]for i in range(m)]  #创建一个m*n的全1矩阵

        for i in range(1,m):
            for j in range(1,n):
                record[i][j] = record[i-1][j]+record[i][j-1]
        return record[m-1][n-1]