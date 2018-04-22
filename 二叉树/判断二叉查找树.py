#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/10 下午4:41

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):

        if root is None:
            return True
        if root.left is None and root.right is None:
            return True

        if root.left:
            if not self.isValidBST(root.left):
                return False
            elif self.max_val(root.left) >= root.val:
                return False

        if root.right:
            if not self.isValidBST(root.right):
                return False
            elif self.min_val(root.right) <= root.val:
                return False

        return True

    def min_val(self, root):
        result = root.val
        while root.left:
            result = root.left.val
            root = root.left
        return result

    def max_val(self, root):
        result = root.val
        while root.right:
            result = root.right.val
            root = root.right
        return result
        # write your code here