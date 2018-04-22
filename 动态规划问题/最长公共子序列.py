#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午3:29

class Solution:
    def longestCommonSubsequence(self,A,B):
        m = len(A)
        n = len(B)
        if m == 0 or n == 0:
            return 0

        record = [[0 for j in range(n+1)]for i in range(m+1)]
        i =1
        while i <= m:
            j=1
            while j <= n:
                if A[i-1] == B[j-1]:
                    record[i][j] = record[i-1][j-1]+1
                else:
                    record[i][j] = max(record[i-1][j],record[i][j-1])
                j += 1
            i += 1
        return record[m][n]

ss = Solution()
result = ss.longestCommonSubsequence([1,2,3],[2,3,1])
print(result)