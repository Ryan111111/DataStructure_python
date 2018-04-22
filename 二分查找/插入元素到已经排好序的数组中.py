#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/11 下午12:48

#对于排好序的数组进行插入的问题，为了减少算法的时间复杂度，用二分查找的方法找到插入的位置

class Solution:
    def searchInsert(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((right+left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid - 1
            else:
                left = mid + 1

        return left

ss = Solution()
result = ss.searchInsert([1,3,5,6],5)
print(result)

