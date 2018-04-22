#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午7:36

#统计n以内的素数个数
def issushu(n):
    k = 0
    for i in range(n):
        count = 0
        for j in range(2,i):
            if i%j == 0:
                count += 1
        if count == 0:
             k += 1
    print(k)
