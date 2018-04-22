#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/30 下午1:54

class Solution:
    def NumberOf1(self,n):
        count = 0
        if n < 0:
            n = n&0xffffffff
        while n:
            count+=1
            n = (n-1)&n
        return count

