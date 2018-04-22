#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/9 下午1:19

"""
快速排序的思想：首先任意去一个数据，通常选取数组的第一个数，作为关键数据，然后将所有比他小的数都放到前面，大的数放到后面

伪代码：1 设置两个变量i，j 排序开始i=0，j=N-1
       2 以第一个数组元素作为关键元素，赋值给key
       3 从j开始向前搜索，由后往前搜索j--，找到第一个小于key的值A[j],将A[j]和A[i]互换
       4 从i开始向后搜索，由前往后搜索i++，找到第一个大雨key的A[i],将A[i]和A[j]互换
       5 重复3，4步，直到i=j，循环结束

时间复杂度：O(nlogn)
"""

def QuickSort(lists,left,right):
    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right
    while left < right:

        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]

        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
    QuickSort(lists,low,left-1)
    QuickSort(lists,left+1,high)
    return lists

A = [1,312,12,14,4,6]
print(QuickSort(A,0,len(A)-1))


