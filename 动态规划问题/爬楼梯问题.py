#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午1:42

class Solution:
    def climbStairs(self,n):
        record = [1,1]  #第1级和第2级的方法
        if n >= 2:
            for i in range(2,n+1):
                record.append(record[i-1]+record[i-2])
        return record[n]