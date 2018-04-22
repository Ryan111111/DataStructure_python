#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/17 下午3:01

def naive_match(s,p):
    m = len(s)
    n = len(p)

    for i in range(m-n+1):
        if s[i:i+n] == p:
            return True
    return False
