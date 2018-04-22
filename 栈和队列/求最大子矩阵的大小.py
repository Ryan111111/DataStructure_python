#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/7 下午4:22

def maxRecSize(map):
    if map == None or len(map)==0 or len(map[0])==0 :
        return 0
    height = [0]*len(map[0])

    for i in range(len(map)):
        for j in range(len(map[0])):
            height[j] += map[i][j]

    return  height

def maxRecFromBottom(height):
    print(height)
    if height == None or len(height) == 0:
        return 0
    maxArea = 0
    Stack = []
    for i in range(len(height)):
        # print(Stack[0])
        Stack.append(i)
        while len(height) != 0 and height[i] <= height[Stack[0]]:
            j = Stack[-1]
            k = -1 if len(Stack) == 0 else Stack[0]
            curArea = (i-k-1)*height[j]    #面积
            maxArea = max(curArea,maxArea)

    while len(Stack) != 0:
        j = Stack[-1]
        k = -1 if len(Stack) == 0 else Stack[0]
        curArea = (len(height)-k-1)*height[j]
        maxArea = max(curArea,maxArea)

    print(maxArea)


map = [[1,0,1,1],[1,1,1,1],[1,1,1,0]]
height = maxRecSize(map)
maxRecFromBottom(height)
