#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/28 下午1:32

class Solution:
    def IsPopOrder(self,pushV,popV):
        result = True
        stack = []

        if len(pushV) != len(popV):
            return False
        for pop in popV:
            if len(stack) and pop == stack[-1]:
                stack.pop()
            else:
                while True:
                    if len(pushV)>0:
                        push = pushV.pop(0)
                        if push == pop:
                            break
                        else:
                            stack.append(push)
                    else:
                        return False
        return result
