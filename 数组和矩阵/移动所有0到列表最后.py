#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/16 下午8:38



def move0tolast(nums):
    stack=[]
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            stack.append(nums[i])
        else:
            count += 1

    for j in range(count):
        stack.append(0)

    print(stack)

move0tolast([1,2,3,0,5,0,4,9,0])
