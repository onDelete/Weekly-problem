#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
用冒泡排序给一个数组排序。输入一个数组，输出排好的数组。

例子：
输入：[3,2,1] 输出：[1,2,3]
输入：[1,5,4,6,7] 输出：[1,4,5,6,7]
输入：[0,2,4,5,7] 输出：[0,2,4,5,7]
输入：[1] 输出：[1]

'''


def solution(arg):
    for i in range(len(arg) - 1):
        for j in range(len(arg) - i - 1):
            if arg[j+1] < arg[j]:
                temp = arg[j]
                arg[j] = arg[j+1]
                arg[j+1] = temp
    return arg

print solution([3,2,1])
print solution([1,5,4,6,7])
print solution([0,2,4,5,7])
print solution([1])
