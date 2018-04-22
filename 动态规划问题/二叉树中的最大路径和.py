#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:06

class Solution:
    def maxPathSum(self,root):
        if root is None:
            return 0
        result = [root.val]
        self.helper(root,result)
        return result[0]

    def helper(self,root,result):
        if root is None:
            return 0

        #由左孩子开始的最长路径
        left_val = self.helper(root.left,result)
        #右孩子开始的最长路径
        right_val = self.helper(root.right,result)

        #计算以root为最高节点的最长路径的长度，并和原先的最大值进行比较
        result[0] = max(result[0],max(left_val,0)+max(right_val,0)+root.val)

        #返回以root为起点的最长路径的长度
        return max(root.val+left_val,root.val+right_val,root.val)