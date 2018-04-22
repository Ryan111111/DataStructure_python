#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/28 下午12:46

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubTree(self,pRoot1,pRoot2):
        result = False                   #设置标识位
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val ==pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1,pRoot2)
            if not result:
                result = self.HasSubTree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubTree(pRoot1.right,pRoot2)
        return result

    def DoesTree1haveTree2(self,pRoot1,pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) \
               and self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)