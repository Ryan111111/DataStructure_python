#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/28 下午12:08
#思路；首先比较两个链表的首结点，那个小的结点则合并到第三个链表尾节点，并向前移动一个结点
#步骤一结果会有一个链表先遍历结束，或者没有
#第三个链表尾结点指向剩余未遍历结束的链表
#返回第三个链表首结点


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self,pHead1,pHead2):
        dummy = ListNode(0)
        pHead = dummy

        while pHead1 and pHead2:
            if pHead1.val >=pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next
            dummy = dummy.next

        if pHead1:
            dummy.next = pHead1
        elif pHead2:
            dummy.next = pHead2

        return pHead.next

