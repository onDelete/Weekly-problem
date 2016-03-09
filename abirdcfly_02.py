#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
给你一串字符串，一个整数代表每行字符的个数，求与其中一个X直接相连（紧挨着）的O最多有多少个？

直接上例子：

输入："OXOOOXOXOXOXXOX"， "5" 输出：3
其图像为：
OXOOO
XOXOX
OXXOX

输入："OXXOXOOXOXOXOOXOOXOX"， "10" 输出：2
其图像为：
OXXOXOOXOX
OXOOXOOXOX

输入："XOOXOOOOOOXOOXOXXXOX"， "5" 输出：4
其图像为：
XOOXO
OOOOO
XOOXO
XXXOX

显而易见，输出最小是0，最大只可能是4.
'''



# # 考虑深度的话
# def solution(str, num):
#     cow = len(str) / num  # 行数
#     newstr = {}  # 为什么[]不可以
#     zmax = 0
#     for i in range(cow):
#         newstr[i] = str[i*num:(i+1)*num]
#     for i in range(cow):  # 先行后列
#         p = 0  # 每行遍历
#         cmax = 0  # 每行最值
#         while p < num:
#             if newstr[i][p] == 'X':
#                 j = p
#                 k = 0
#                 while j != 0 and newstr[i][j-1] != 'X':
#                     j -= 1
#                     k += 1
#                     if j == 0:
#                         break
#                 j = p
#                 while j != num-1 and newstr[i][j+1] != 'X':
#                     k += 1
#                     j += 1
#                     if j == num:
#                         break
#                 j = i
#                 while j != 0 and newstr[j-1][p] != 'X':
#                     j -= 1
#                     k += 1
#                     if j == 0:
#                         break
#                 j = i
#                 while j != cow - 1 and newstr[j+1][p] != 'X':
#                     j += 1
#                     k += 1
#                     if j == cow:
#                         break
#                 if k > cmax:
#                     cmax = k
#             p += 1
#             if cmax > zmax:
#                 zmax = cmax
#     return zmax
#
#
# print solution("OXOOOXOXOXOXXOX", 5) # 5
# print solution("OXXOXOOXOXOXOOXOOXOX", 10) # 4
# print solution("XOOXOOOOOOXOOXOXXXOX", 5) #5

# 上下左右只考虑一层
def solution(str, num):
    cow = len(str) / num  # 行数
    newstr = {}  # 为什么[]不可以
    zmax = 0
    for i in range(cow):
        newstr[i] = str[i*num:(i+1)*num]
    for i in range(cow):  # 先行后列
        p = 0  # 每行遍历
        cmax = 0  # 每行最值
        while p < num:
            if newstr[i][p] == 'X':
                j = p
                k = 0
                if j != 0 and newstr[i][j-1] != 'X':
                    k += 1
                j = p
                if j != num-1 and newstr[i][j+1] != 'X':
                    k += 1
                j = i
                if j != 0 and newstr[j-1][p] != 'X':
                    k += 1
                j = i
                if j != cow - 1 and newstr[j+1][p] != 'X':
                    k += 1
                if k > cmax:
                    cmax = k
            p += 1
            if cmax > zmax:
                zmax = cmax
    return zmax

# 改进两方向遍历，O(n)算法类似01题改进算法。参见abirdcfly_01.py

print solution("OXOOOXOXOXOXXOX", 5)  # 3
print solution("OXXOXOOXOXOXOOXOOXOX", 10)  # 2
print solution("XOOXOOOOOOXOOXOXXXOX", 5)  # 4
