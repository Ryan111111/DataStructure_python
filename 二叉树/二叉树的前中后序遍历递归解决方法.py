#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/16 下午2:03
class BinaryTreeNode(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.right = right
        self.left = left

class BinaryTree(object):
    def __init__(self,root=None):
        self.root = root
    def is_empty(self):
        return self.root == None

    def preOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        #先根节点，左节点，右节点
        print(BinaryTreeNode.data)
        self.preOrder(BinaryTreeNode.left)
        self.preOrder(BinaryTreeNode.right)

    def midOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        #左节点，根节点，右节点
        self.midOrder(BinaryTreeNode.left)
        print(BinaryTreeNode.data)
        self.midOrder(BinaryTreeNode.right)

    def postOrder(self,BinaryTreeNode):
        if BinaryTreeNode == None:
            return
        #左节点,右节点,根节点
        self.postOrder(BinaryTreeNode.left)
        self.postOrder(BinaryTreeNode.right)
        print(BinaryTreeNode.data)

n1 = BinaryTreeNode(data="D")
n2 = BinaryTreeNode(data="E")
n3 = BinaryTreeNode(data="F")
n4 = BinaryTreeNode(data="B", left=n1, right=n2)
n5 = BinaryTreeNode(data="C", left=n3, right=None)
root = BinaryTreeNode(data="A", left=n4, right=n5)

bt = BinaryTree(root)
print('先序遍历')
bt.preOrder(bt.root)
print('中序遍历')
bt.midOrder(bt.root)
print('后序遍历')
bt.postOrder(bt.root)
