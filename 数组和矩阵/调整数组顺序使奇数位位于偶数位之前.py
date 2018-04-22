#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/30 下午2:18

class Solution:
    def reOrderArray(self,array):
        stack1 = []
        stack2 = []
        for i in array:
            if i%2 == 0:
                stack2.append(i)
            else:
                stack1.append(i)
        stack1 += stack2
        return stack1


    def reOrderArray1(self,array):
        pk = 0 #奇数所要插入的位置
        for i in range(len(array)):
            if array[i]%2 != 0:
                j = i
                while j > pk:
                    temp = array[j-1]
                    array[j-1] = array[j]
                    array[j] = temp
                    j -= 1

                pk += 1
        return array
