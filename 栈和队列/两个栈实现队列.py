#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/30 下午1:27

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self,node):
        self.stackA.append(node)
    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append((self.stackA.pop()))
            return self.stackB.pop()
