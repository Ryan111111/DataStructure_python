#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午6:48

#通过判断递归的判断

class Solution:
    def isSameTree(self,p,q):
        if p and q:
            if p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False
        return p is q
