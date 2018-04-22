#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/31 下午12:10

#通过递归的方式进行

class Solution:
    def TreeDepth(self,pRoot):
        if pRoot==None:return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1