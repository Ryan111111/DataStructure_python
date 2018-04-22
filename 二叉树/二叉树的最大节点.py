#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/26 下午5:11

class Solution:
    maxNum = -9999
    node = None

    def maxNode(self,root):
        if root is None:
            return None
        self.max(root)
        return self.node

    def max(self,root):
        if root is None:
            return None
        if root.val > self.maxNum:
            self.maxNum = root.val
            self.node = root
        self.max(root.left)
        self.max(root.right)
