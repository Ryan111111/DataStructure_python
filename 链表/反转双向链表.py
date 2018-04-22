#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/1 下午2:26

class ListNode(object):
    def __init__(self,data):
        self.data = data
        self.pre = None
        self.next = None

def RverseDoubleList(head):
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        head.pre = next
        pre = head
        head = next
    return pre

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)

head.next = p1
p1.next = p2
p1.pre = head

newhead = None
pre = RverseDoubleList(head)
while pre:
    print(pre.data)
    pre = pre.next