#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/26 下午2:52
class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.pre = None
        self.next = None

    #初始化双向链表
def __init__(self):
    head = Node()
    tail = Node()
    self.head = head
    self.tail = tail
    self.head.next = self.tail
    self.tail.pre = self.head

#获取链表长度
def __len__(self):
    length = 0
    node = self.head
    while node.next != self.tail:
        length += 1
        node = node.next
    return length

#追加结点
def append(self,data):
    node = Node(data)
    pre = self.tail.pre
    pre.next = node
    node.pre = pre
    self.tail.pre = node
    node.next = self.tail
    return node

#获取结点,获取第index个值，若index>0正向获取else 反向获取
def get(self,index):
    length = len(self)
    index = index if index >= 0 else length + index
    if index >= length or index < 0: return None
    node = self.head.next
    while index:
        node = node.next
        index -= 1
    return node

#删除结点
def delete(self,index):
    node = self.get(index)
    if node:
        node.pre.next = node.next
        node.next.pre = node.pre
        return True
    return False





