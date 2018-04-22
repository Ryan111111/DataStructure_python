#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/28 下午1:07

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromToptoBottom(self,root):
        if not root:
            return []
        queue = []
        result = []

        queue.append(root)  #根节点放入队列
        while len(queue)>0:
            node = queue.pop(0)      #取出当前的子节点
            result.append(node.val)  #添加层次遍历的结果
            if node.left:
                queue.append(node.left)  #如果左子树存在，放入队列
            if node.right:
                queue.append(node.right) #然后将右子树放入队列
        return result