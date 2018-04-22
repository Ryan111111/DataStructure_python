#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午2:48

#机器人从左上方走到右下方一共有过多少中走法
#核心在于上一步的状态转移方程


class Solution:
    def uniquePaths(self,m,n):
        if m < 1 or n < 1:
            return 0
        record = [[1 for i in range(n)]for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                record[i][j] = record[i-1][j]+record[i][j-1]
        return record[m-1][n-1]