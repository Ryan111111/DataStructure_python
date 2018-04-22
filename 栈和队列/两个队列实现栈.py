#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/30 下午1:33

class Solution:
    def __init__(self):
        self.queueA = []
        self.queueB = []
    def push(self,node):
        self.queueA.append(node)
    def pop(self):
        if len(self.queueA) == 0:
            return None
        while len(self.queueA) != 1:
            self.queueB.append(self.queueA.pop(0))
        self.queueA,self.queueB = self.queueB,self.queueA
        return self.queueB.pop()
