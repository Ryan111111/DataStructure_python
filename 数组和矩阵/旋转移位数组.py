#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午12:43


#给定循转的位数，将数组元素循环移位

class Solution:
    def rotate(self,nums,k):
        n = len(nums)
        nums[:] = nums[n-k:]+nums[:n-k]
        print(nums)