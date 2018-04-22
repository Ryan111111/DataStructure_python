#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午3:26

class Solution:
    def findMaxConsecutiveOnes(self,nums):
        count = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                max = max(max,count)
            else:
                count = 0

        return max




