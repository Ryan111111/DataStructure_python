#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/6 下午2:12

#暴力解法
def fb(n):
    if n < 1:
        return 0
    elif n==1 and n==2:
        return 1
    return fb(n-1)+fb(n-2)

def fb2(n):
    if n < 1:
        return 0
    elif n==1 and n==2:
        return 1

    res = 1
    pre = 1
    tmp = 0

    for i in range(3,n):
        tmp = res
        res = res+pre
        pre = tmp

    return res

