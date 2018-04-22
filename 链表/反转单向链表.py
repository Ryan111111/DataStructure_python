#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/27 上午11:53

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def RverseList(head):
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)

head.next = p1
p1.next = p2

newhead = None
pre = RverseList(head)
while pre:
    print(pre.val)
    pre = pre.next

