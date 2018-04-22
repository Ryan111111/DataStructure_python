#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午3:36

class Solution:
    def longestCommomSubString(self,A,B):
        m = len(A)
        n = len(B)
        if m==0 or n==0:
            return 0

        record = [[0 for j in range(n+1)] for i in range(m+1)]

        i = 1
        temp = 0

        while i <= m:
            j = 1
            while j <= n:
                if A[i-1]==B[j-1]:
                    record[i][j] = record[i-1][j-1] + 1
                j += 1
            temp = max(max(record[i]),temp)
            i+=1
        return temp