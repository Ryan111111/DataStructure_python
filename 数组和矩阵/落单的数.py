#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午8:05

class Solution:
    def singleNumber(self,A):
        result = 0
        for i in A:
            result ^= i
        return result

    def singleNumber3(self,A):
        result = 0
        record = [0 for i in range(32)]

        for i in A:
            #对32为二进制串从右往左扫描
            for index in range(-1,-32,-1):
                #temp为每一位代表的数字（0，1）
                temp = (i&1)
                record[index] += temp
                record[index] %= 3
                i = i >> 1

        for i in range(32):
            result += record[31-i]*pow(2,i)
        return result