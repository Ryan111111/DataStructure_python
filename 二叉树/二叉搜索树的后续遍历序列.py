#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/28 下午2:42

class Solution:
    def VerifySquenceOfBST(self,sequence):
        if sequence==None or len(sequence)==0:
            return False
        length = len(sequence)
        root = sequence[length-1]  #最后一个点是根节点

        #在二叉搜索树，左子树点小于根节点
        for i in range(length):
            if sequence[i]>root:
                break

        #在二叉搜索树，右子树点大于根节点
        for j in range(i,length):
            if sequence[j]<root:
                return False

        #判断左子树是否为二叉树
        left = True
        if i>0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        #判断右子树是否为二叉树
        right = True
        if i<length-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

