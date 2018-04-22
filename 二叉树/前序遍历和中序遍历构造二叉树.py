#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Ryan
# @Time: 2018/3/27 下午1:35

#思路：前序遍历的结果中，第一个结点一定是根结点，然后在中序遍历的结果中查找这个根节点
#根结点左边就是左子树，根结点右边就是右子树，递归的构造出左右子树即可

class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def construct_tree(pre_order,mid_order):
    if len(pre_order)==0:
        return None
    root_data = pre_order[0]
    #遍历找到根结点
    for i in range(0,len(mid_order)):
        if mid_order[i] == root_data:
            break
        #递归构造左右子树
    left = construct_tree(pre_order[1:1+i],mid_order[:i])
    right = construct_tree(pre_order[1+i:],mid_order[1+i:])
    return Node(root_data,left,right)

if __name__ == '__main__':
  pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
  mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
  root = construct_tree(pre_order, mid_order)
  print(root.data)

