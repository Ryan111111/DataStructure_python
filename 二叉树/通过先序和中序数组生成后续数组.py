#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/8 下午2:59
def preInToPos(pre, mid):
    def preInPos(pre, pi, pj, mid, mi, mj, pos, sj, map):
        if pi > pj:
            return sj
        pos[sj] = pre[pi]
        sj -= 1
        index = map.get(pre[pi])
        sj = preInPos(pre, pi+index-mi+1, pj, mid, index+1, mj, pos, sj, map)
        return preInPos(pre, pi+1, pi+index-mi, mid, mi, index-1, pos, sj, map)


    if pre == None or mid == None:
        return []
    pos = [None for i in range(len(mid))]
    map = {}
    for i in range(len(mid)):
        map[mid[i]] = i
    preInPos(pre, 0, len(pre)-1, mid, 0, len(mid)-1, pos, len(mid)-1, map)
    return pos