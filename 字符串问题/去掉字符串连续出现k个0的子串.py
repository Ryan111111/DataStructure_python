#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/6 下午6:46

def removeKZeros(str,k):
    if str == None or k < 1:
        return str
    str_toArray = list(str)
    count = 0
    start = -1

    #按照原理将满足删除条件的字符0编程数字0
    for i in range(len(str_toArray)):
        if str_toArray[i] == '0':
            count += 1
            if start == -1:
                start = i
        else:
            if count == k:
                while count != 0:
                    count -= 1
                    str_toArray[start] = 0
                    start += 1
            count = 0
            start = -1
    #处理字符尾尾部满足条件的情况
    if count == k:
        while count != 0:
            count -= 1
            str_toArray[start] = 0
            start += 1

    #返回一个删除后的字符
    result_list = []
    for j in range(len(str_toArray)):
        if str_toArray[j] != 0:
            result_list.append(str_toArray[j])
    result = ''.join(result_list)

    print(result)


removeKZeros('A0000B000A000B000',3)