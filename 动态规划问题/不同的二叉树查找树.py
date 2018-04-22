#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:21

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        record = [0 for i in range(n + 1)]
        record[0] = 1
        i = 1
        while i <= n:
            j = 0
            while j < i:
                record[i] += record[j] * record[i - 1 - j]
                j += 1
            i += 1
        return record[n]
        # write your code here