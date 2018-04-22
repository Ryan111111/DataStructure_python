#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:51

class Solution:
    def intersection(self,nums1,nums2):
        return list(set(nums1)&set(nums2))

    def intersection2(self, nums1, nums2):
        hash_table = {}
        result = []
        hash_table.fromkeys(nums1)
        for i in nums2:
            if len(hash_table) == 0:
                break
            if i in hash_table:
                result.append(i)
                hash_table.pop(i)
        return result
