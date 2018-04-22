#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/7 下午1:59

def rotate(matrix):
    tR = 0
    tC = 0
    dR = len(matrix)-1
    dC = len(matrix[0])-1
    while tR < dR:
        rotateEdge(matrix,tR,tC,dR,dC)
        tR += 1
        tC += 1
        dR -= 1
        dC -= 1

    print(matrix)

def rotateEdge(m,tR,tC,dR,dC):
    times = dC - tC   #总的组数
    for i in range(times):
        temp = m[tR][tC+i]
        m[tR][tC+i] = m[dR-i][tC]
        m[dR-i][tC] = m[dR][dC-i]
        m[dR][dC-i] = m[tR+i][dC]
        m[tR+i][dC] = temp


rotate([[1,2,3],[4,5,6],[7,8,9]])

