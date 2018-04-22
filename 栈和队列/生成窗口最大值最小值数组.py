#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/7 下午3:43
def getMaxMinWindow(arr,k):
    if arr == None or k<1 or len(arr)<k:
        return
    dequeMax = []
    dequeMin = []

    resMax = []
    resMin = []

    for i in range(len(arr)):
        while dequeMax and arr[dequeMax[-1]] <= arr[i]:
            dequeMax.pop()
        while dequeMin and arr[dequeMin[-1]] >= arr[i]:
            dequeMin.pop()

        dequeMax.append(i)
        dequeMin.append(i)

        if dequeMax[0] == i-k:
            dequeMax.pop(0)
        if dequeMin[0] == i-k:
            dequeMin.pop(0)
        if i-k+1 >= 0:
            resMax.append(arr[dequeMax[0]])
            resMin.append(arr[dequeMin[0]])

    result = []
    for i in range(len(resMax)):
        result.append(resMax[i]-resMin[i])
    print(result)