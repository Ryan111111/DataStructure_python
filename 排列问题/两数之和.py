#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午2:25

class Solution:
    def twoSum(self,numbers,target):
        #生成一张哈希表
        hash_table = {}
        for i,ele in enumerate(numbers):
            hash_table[ele] = i

        for i,ele in enumerate(numbers):
            gap = target-ele
            if gap in hash_table.keys():
                return [i+1,hash_table[gap]+1]