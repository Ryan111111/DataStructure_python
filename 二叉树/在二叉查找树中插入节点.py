#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:28

class Solution:
    def insertNode(self,root,node):
        if root is None:
            root = node
        elif root.val > node.val:
            root.left = self.insertNode(root.left,node)
        elif root.val < node.val:
            root.right = self.insertNode(root.right,node)
        return root