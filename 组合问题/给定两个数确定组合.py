#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午12:25

class Solution:
    def combine(self,n,k):
        path = []
        reuslt = []
        begin = 1
        self.helper(k,begin,n,path,reuslt)
        return reuslt

    def helper(self,k,begin,n,path,result):
        if len(path) == k:
            temp = path[:]
            result.apppend(temp)
            return

        #遍历从cur到最后的数字
        for i in range(begin,n+1):
            path.append(i)
            self.helper(k,i+1,n,path,result)
            path.remove(i)