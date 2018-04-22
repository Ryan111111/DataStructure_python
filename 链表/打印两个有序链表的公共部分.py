#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/4/1 下午12:21

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist(object):
    def __init__(self):   #初始化链表
        self.head = None
    def __len__(self):    #获取链表长度
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node

    def travel_List(self):    #遍历链表
        if self.__len__() == 0:
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)




def Two_Node_PublicPart(head1,head2):
    while(head1 and head2):
        if (head1.data < head2.data):
            head1 = head1.next
        elif(head1.data > head2.data):
            head2 = head2.next
        else:
            print(head1.data)
            head1 = head1.next
            head2 = head2.next

head1 = Linklist()
head2 = Linklist()

head1.append(1)
head1.append(2)
head1.append(3)

head2.append(4)
head2.append(2)
head2.append(3)

# print(head1.travel_List())
print(head1.data)

Two_Node_PublicPart(head1,head2)




