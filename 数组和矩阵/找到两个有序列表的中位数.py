#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/12 下午8:38

#!usr/bin/env python
#encoding:utf-8

'''
__Author__:沂水寒城
功能：找到两个有序列表的中位数
若列表总长度为奇数则直接返回中间下标的值
否则返回前一个值，如长度为6则返回下标为2处的值
'''

import random

def random_nums_genetor(max_value=1000, total=100):
    '''
    生成随机数
    '''
    num_list=[]
    for i in range(total):
        num_list.append(random.randint(1,max_value))
    return num_list


def find_two_list_mid_num(num_list1,num_list2):
    '''
    找到两个有序列表的中位数
    '''
    length1=len(num_list1)
    length2=len(num_list2)
    total=length1+length2
    if total%2==0:
        half=total/2-1
    else:
        half=total/2
    res_list=[]
    while len(num_list1) and len(num_list2):
        if num_list1[0]<num_list2[0]:
            res_list.append(num_list1.pop(0))
        else:
            res_list.append(num_list2.pop(0))
    if len(num_list1):
        res_list+=num_list1
    elif len(num_list2):
        res_list+=num_list2
    #print res_list
    print (res_list[half])
    return res_list

#随机函数是用来生成样例的
