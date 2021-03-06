#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午1:36

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
            return False
        if num==1:
            return True
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /=5
        return num == 1
