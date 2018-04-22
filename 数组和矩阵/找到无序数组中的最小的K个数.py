#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/7 下午2:19

def getMinKNumsByHeap(arr,k):
    if k<1 or k>len(arr):
        return arr


    #构建一个大小为K的大根堆
    kHeap = []
    for i in range(k):
        heapInsert(kHeap,arr[i],i)

    #根据数组维护更新大根堆
    for j in range(k,len(arr)):
        if arr[j] < kHeap[0]:
            kHeap[0] = arr[j]
            heapify(kHeap,0,k)

    return kHeap

def heapify(arr,index,heapSize):
    left = index*2+1
    right = index*2+2
    largest = index

    while left<heapSize:
        if arr[left]<arr[index]:
            largest = left
        elif right<heapSize and arr[right]>arr[largest]:
            largest = right
        elif largest != index:
            swap(arr,largest,index)
        else:
            break
        index = largest
        left = index*2+1
        right = index*2+2

#大根堆的插入操作
def heapInsert(arr,value,index):
    arr[index] = value
    while index != 0:
        parent = (index-1)/2
        if arr[parent] < arr[index]:
            swap(arr,parent,index)
            index= parent
        else:
            break

#交换操作
def swap(arr,index1,index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

result = getMinKNumsByHeap([2,3,4,5,6,7,8],3)
print(result)
