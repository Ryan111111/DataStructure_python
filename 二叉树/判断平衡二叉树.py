#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/26 下午8:50

#定义：若左右子树深度差不多超过1则为一颗平衡二叉树
#思路
# 1.使用获取二叉树深度的方法来获取左右子树的深度
# 2.左右深度相减，若大于1返回false
# 3.通过递归对每个节点进行判断，若全部均未返回False，则返回True

class Solution:
    def getDeepth(self,Root):
        if Root is None:
            return 0
        nright = self.getDeepth(Root.right)
        nleft = self.getDeepth(Root.left)
        return max(nright,nleft)+1
    def IsBalanced_Solution(self,pRoot):
        if pRoot is None:
            return True
        right = self.getDeepth(pRoot.right)
        left = self.getDeepth(pRoot.left)
        if abs(right-left)>1:
            return False
        return self.IsBalanced_Solution(pRoot.right) and self.IsBalanced_Solution(pRoot.left)