#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午12:59

class Solution:
    def backPack(self,m,A):
        n = len(A)
        if n == 0:
            return 0
