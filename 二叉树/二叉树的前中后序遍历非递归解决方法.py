#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/16 下午2:39

class TreeNode:
    def __init__(self,value=None,leftNode=None,rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

class Tree:
    def __init__(self,root=None):
        self.root = root

    def preOrder(self):
        if not self.root:
            return
        stackNode = []
        stackNode.append(self.root)
        while stackNode:
            node = stackNode.pop()
            print(node.value)
            if node.rightNode:
                stackNode.append(node.rightNode)
            if node.leftNode:
                stackNode.append(node.leftNode)

    def midOrder(self):
        if not self.root:
            return
        stack = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.leftNode
            node = stack.pop()
            print(node.value,)
            node = node.rightNode

    def posOrder(self):
        if not self.root:
            return
        stack1 = []
        stack2 = []

        stack1.append(self.root)
        while stack1:
            head = stack1.pop()
            stack2.append(head)
            if head.leftNode != None:
                stack1.append(head.leftNode)
            elif head.rightNode != None:
                stack1.append(head.rightNode)

        while stack2:
            print(stack2.pop().value)
#后续非递归是最难的，经常会考察
"""
后续遍历根结点，先遍历左子树，然后遍历右子树，此时反过来想，
先遍历根结点，然后遍历右子树，最后左子树，这样就转化为一个先序遍历的类型，
最后只把遍历结果逆序输出就ok，而先序遍历是比较好理解的
1.使用栈存储结点
2。当结点不存在或者栈不为空，判断结点
3。当结点存在，结点值保存，结点入栈，并将指针指向结点的右子树
4。当栈不为空，结点出栈，并将指针指向左子树
5。重复2-4知道结果产生
6。逆序输出结果
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder(root):
    ret = []
    stack = []
    while root or stack:
        while root:
            ret.append(root.val)
            stack.append(root)
            root = root.right
        if stack:
            top = stack.pop()
            root = top.left
    return ret[::1]

