#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/16 下午9:13

#思路：第一轮，在r1-r[n]中选择最小的记录与r1交换
#     第二轮，在r2-r[n]中选择最小的记录与r2交换

def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if lists[min]>lists[j]:
                min = j
        lists[min],lists[i] = lists[i],lists[min]
    return lists

