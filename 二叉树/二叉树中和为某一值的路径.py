#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/31 下午12:03

#递归先序遍历，把结点加入路径
#若该结点是叶子节点则比较当前路径是否等于期待和
#弹出结点，每一轮递归返回到父节点，当前路径也应该回退一个结点

class Solution:
    def FindPath(self,root,expectNumber):
        if not root:
            return []
        result = []

