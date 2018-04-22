#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午4:38

class Solution:
    def maxSubArray(self,nums):
        max_value = nums[0]
        temp_sum = 0
        for i in nums:
            temp_sum += i
            max_value = max(max_value,temp_sum)
            temp_sum = max(temp_sum,0)   #这个0比较精髓，temp_sum有可能为负
        return max_value

nums = [-2, 11, -4, 13, -5, -2]
ss = Solution()
result = ss.maxSubArray(nums)
print(result)