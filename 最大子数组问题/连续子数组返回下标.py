#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:38

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        max_value, sum_value = A[0], 0
        index, n = 0, len(A)
        t1, t2 = 0, 0
        temp = 0
        while index < n:
            sum_value += A[index]
            if sum_value > max_value:
                t1 = temp
                t2 = index
                max_value = sum_value
            if sum_value < 0:
                temp = index + 1
                sum_value = 0
            index += 1
        return [t1, t2]
        # Write your code here