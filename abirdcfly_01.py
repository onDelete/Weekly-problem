#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
问题1： 一维OX

给你一串包含'X'和'O'字符串，如"OXOOOXXXOXXOOOXXXOXO",问这个字符串中，与其中一个X直接相连（中间没有X格着）的O最多有多少个？比如"OXOO",就有三个O与X相连。但是"OXOOOXOO"最多就是五个而不是六个，因为左边的X挡住了最左边的O。

输入：字符串 输出：整数

例子：
输入:"OXO"            输出：2
输入:"OXOOXOXXOOOXO"  输出：4
输入:"OOXOOOXOXO"     输出：5
输入:"OOOOOOOOOO"     输出：0
输入:"XXX"            输出：0
'''


def solution(str):
    i = 0
    amax = 0
    while i < len(str):
        if str[i] == 'X':
            j = i
            k = 0
            while j != 0 and str[j-1] != 'X':
                j -= 1
                k += 1
                if j == 0:
                    break
            j = i
            while j != len(str)-1 and str[j+1] != 'X':
                k += 1
                j += 1
                if j == len(str):
                    break
            if k > amax:
                amax = k
        i += 1
    return amax




str ='OXO'
print solution(str)
str ='OXOOXOXXOOOXO'
print solution(str)
str ='OOXOOOXOXO'
print solution(str)
str ='OOOOOOOOOO'
print solution(str)
str ='XXX'
print solution(str)
