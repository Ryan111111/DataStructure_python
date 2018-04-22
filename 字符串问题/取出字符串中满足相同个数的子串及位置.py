#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/7 下午2:43

input = 'abbcccddeefffgggcc'
k = 2

def getSameNumStr(input_str,k):
    if input_str == None or k < 1:
        return input_str

    str_toArray = list(input_str)

    #初始化计数，以及开始的位置
    count = 0
    start = -1

    temp_char = str_toArray[0]
    result = []

    #循环遍历数组
    for i in range(1,len(str_toArray)):
        if str_toArray[i] == temp_char:
            count += 1
            if start == -1:
                start = i-1
        else:
            if count == k-1:
                result.append(start)

            temp_char = str_toArray[i]
            count = 0
            start = -1

    if count == k-1:
        result.append(start)

    print(result)

getSameNumStr(input,k)


