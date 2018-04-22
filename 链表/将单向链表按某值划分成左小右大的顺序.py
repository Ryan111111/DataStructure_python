#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/2 下午12:49

class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def listPartition(head,pivot):
    if head == None:
        return head

    cur = head
    nodeArr =[]
    while cur:
        nodeArr.append(cur.data)
        cur = cur.next
    print(nodeArr)

    arrPartition(nodeArr,pivot)
    print(nodeArr)


#实现快排的函数
def arrPartition(nodeArr,pivot):
    small = -1
    big = len(nodeArr)
    index = 0
    while index != big:
        if nodeArr[index] < pivot:
            small += 1
            swap(nodeArr,small,index)
            index += 1
        elif nodeArr[index] == pivot:
            index += 1
        else:
            big -= 1
            swap(nodeArr,big,index)

#实现交换的功能
def swap(nodeArr,a,b):
    tmp = nodeArr[a]
    nodeArr[a] = nodeArr[b]
    nodeArr[b] = tmp


head1 = ListNode(9)
p1 = ListNode(0)
p2 = ListNode(4)
p3 = ListNode(5)
p4 = ListNode(1)

head1.next = p1
p1.next = p2
p2.next = p3
p3.next = p4

print(listPartition(head1,3))