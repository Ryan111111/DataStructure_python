#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/29 上午11:46

class Solution:
    def Convert(self,pRootOfTree):
        if not pRootOfTree:return
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i,v in enumerate(self.arr[:-1]):
            v.right = self.arr[i+1]
            self.arr[i+1].left = v
        return self.arr[0]

    def midTraversal(self,root):
        if not root:return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)