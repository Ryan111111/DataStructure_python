#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午1:26

#采用除余结合的思想，要考虑26%26为0，

class Solution(object):
    #列数转换乘数字
    def convertToTitle(self,n):
        res = ''
        while n:
            res = chr((n-1)%26 + ord('A')) + res
            n = int((n-1)/26)
        return res

    #数字转化乘字母
    def titletoNumber(self,s):
        res = 0
        for num in s:
            res = res*26 + (ord(num)-ord('A')+1)
        return res



ss = Solution()
result = ss.convertToTitle(27)
print(result)

result1 = ss.titletoNumber('AA')
print(result1)