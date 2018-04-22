#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/17 下午3:03

#KMP算法的想法是，不要把搜索位置一会已经比较过的位置，激素把它向后移动，这样就能提高效率

#KMP
def kmp_match(s, p):
    m = len(s); n = len(p)
    cur = 0#起始指针cur
    table = partial_table(p)
    while cur<=m-n:
        for i in range(n):
            if s[i+cur]!=p[i]:
                cur += max(i - table[i-1], 1)#有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True
    return False

#部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1,len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i+1] for j in range(1,i+1)}
        ret.append(len((prefix&postfix or {''}).pop()))
    return ret
