#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-23 19:24:57
# @Author  : Allen Young (allenyoung717@gmail.com)
# @Version : $Id$

# 破解密码

def decodefun(string, lst, num):    
    for i in range(num): 
        string_lst = [string[j] for j in lst]
        string=''.join(string_lst)

    return string

flag = False

while not flag:
    string = raw_input('Please input string: ')
    string_len = len(string)
    lst = raw_input('Please input the array, using space to separate, tap the Enter to end: ')
    lst = map(int, lst.split())
    lst_len = len(lst)
    if string_len == lst_len: # 判断输入的字符串和数组是否对应
        flag = True
        num = input('Please input a number: ')
    else:
        print 'the input string and list are not matched, please input again!'


print 'The decoded string is: ', decodefun(string, lst, num)

# test
# print
# print 'the following is for test'
# string = 'ABC'
# lst = [2, 0, 1]
# num = 2
# print 'Input:"ABC" [2,0,1] 2, the output should be "BCA", the function return:', decodefun(string, lst, num)

# string = 'ABCD'
# lst = [3, 2, 1, 0]
# num = 1
# print 'Input:"ABCD" [3, 2, 1, 0] 1, the output should be "DCBA", the function return:', decodefun(string, lst, num)

# string = '12345'
# lst = [3, 1, 2, 4, 0]
# num = 1
# print 'Input:"12345" [3, 1, 2, 4, 0] 1, the output should be "42351", the function return:', decodefun(string, lst, num)


