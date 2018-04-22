#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/17 下午3:48

def find_child(target,C):
    ret = []

    for child_index in range(len(C)):
        child = C[child_index]
        if child == target:
            ret.append([child])
        elif child < target:
            ret_list = find_child(target-child,C)
            for child_list_temp in ret_list:
                child_list_temp.append(child)
                ret.append(child_list_temp)
        else:
            pass
    return ret
