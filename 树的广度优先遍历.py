#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/24 上午11:43

import queue

class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root
    def breathSearch(self):
        if self.root == None:
            return None
        retList = []
        q = queue.Queue()   #创建了一个队列
        q.put(self.root)    #将根结点放入队列中
        #只要队列不为空，则遍历节点，并分别把左子节点和右子节点放入列表中
        while q.empty() is not True:
            node = q.get()
            retList.append(node.var)

            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        return retList




