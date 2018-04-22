#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/2 下午12:01

#思路：利用栈读取链表元素，然后顺序就是相仿的，回文的话，两个是一样的

class ListNode:
    def __init__(self,x):
        self.data = x
        self.next = None

def isPalindrome(head):
    #实现从链表中读取数据，压入栈中
    stack = []
    cur = head
    while cur:
        stack.append(cur.data)
        cur = cur.next
    stack = stack[::-1]  #利用简单的列表构成一个栈

    i = 0
    while head != None:
        if head.data != stack[i]:
            return False
        head = head.next
        i += 1
    return True

head1 = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(3)
p4 = ListNode(1)

head1.next = p1
p1.next = p2
p2.next = p3
p3.next = p4


# print(isPalindrome(head1))



