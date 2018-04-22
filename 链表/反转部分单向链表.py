#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/1 下午3:02


class ListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def RverseList(head):
    pre = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        count = 1
        # 找到要翻转部分的开始
        while count != m:
            pre = pre.next
            count += 1
        # gap为循环的次数
        gap = n - m + 1
        # 第二部分
        second = pre.next
        # 设置第一部分的尾节点，目的在于最后的合并
        tail = second
        pre.next = None
        while gap != 0:
            cur = second
            second = second.next
            temp = pre.next
            pre.next = cur
            cur.next = temp
            gap -= 1
        # 两部分合并
        tail.next = second
        return dummy.next
        # write your code here




head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)

head.next = p1
p1.next = p2
p2.next = p3

while head:
    print(head.data)
    head = head.next

re = Solution()


node2 = re.reverseBetween(head,2,3)
while node2:
    print(node2.data)
    node2 = node2.next

