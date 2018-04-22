#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午1:53

class Solution:
    def permute(self,nums):
        result = []
        if nums is None:
            return result
        if len(nums) == 0:
            result.append([])

        for ele in nums:
            temp_nums = nums[:]
            temp_nums.remove(ele)
            for i in self.permute(temp_nums):
                i.insert(0,ele)
                result.append(i)
        return  result

ss = Solution()
print(ss.permute([1,2,3]))
