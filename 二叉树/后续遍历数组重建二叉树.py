#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/6 下午1:26

#判断这个数组，是不是某二叉树的后续遍历

def isPostArray(arr):
    if arr == None or len(arr)==0:
        return False
    return isPost(arr,0,len(arr)-1)

def isPost(arr,start,end):
    if len(arr)-1 == 0:
        return True
    less = -1
    more = end

    for i in range(end):
        if (arr[end] > arr[i]):
            less = i
        elif more == end:
            more = i

    if (less == -1 and more == end):
        return isPost(arr,start,end-1)
    if (less != more - 1):
        return False

    return isPost(arr,start,less) & isPost(arr,more,end-1)