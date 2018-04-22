#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/9 下午1:37

def factorial(num):
    if num == 0:
        return 0
    result = 1
    for i in range(1,num+1):
        result *= i
    return result
