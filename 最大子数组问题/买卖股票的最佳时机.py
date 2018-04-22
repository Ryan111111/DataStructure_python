#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午7:21

class Solution:
    def maxProfit(self,prices):
        if len(prices) <= 1:
            return 0

        n = len(prices)
        sum_value = 0
        max_value = 0

        for i in range(1,n):
            sum_value +=prices[i]-prices[i-1]
            max_value = max(max_value,sum_value)
            sum_value = max(0,sum_value)

        return max_value