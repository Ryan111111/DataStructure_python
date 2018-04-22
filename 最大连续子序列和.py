#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/22 下午2:03


#暴力解法O（n^2）

def manSum(list):
    maxsum = list[0]
    for i in range(len(list)):
        maxtmp = 0
        for j in range(i,len(list)):
            maxtmp += list[i]
            if maxtmp > maxsum:
                maxsum = maxtmp
    return maxsum

#动态规划，假设数据a[i]，因为最大连续的子序列和必须在位置0，n-1之间的某个位置结束，
# 那么当循环遍历到第i个位置时，如果其前面的连续子序列和小于等于0，那么以位置i结尾的最大连续子序列和就是第i个位置的值
# 如果其前面的连续子序列和大于0，则以位置i结尾的最大连续子序列和为b[i] = max{b[i-1]+a[i],a[i]}
def maxSum(list_of_nums):
    maxsum = 0
    maxtmp = 0
    for i in range(len(list_of_nums)):
        if maxtmp <= 0:
            maxtmp = list_of_nums[i]
        else:
            maxtmp +=list_of_nums[i]

        if (maxtmp > maxsum):
            maxsum = maxtmp
    return maxsum

list_of_num = [1,3,-3,4,-6]
print(maxSum(list_of_num))