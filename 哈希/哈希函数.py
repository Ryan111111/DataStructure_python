#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午1:52

class Solution:
    def hashCode(self,key,HASH_SIZE):
        temp = 0
        i,n = 0,len(key)
        while i < n:
            temp = (temp*33)%HASH_SIZE
            temp = (temp+ord(key[i]))%HASH_SIZE
            i += 1
        return temp