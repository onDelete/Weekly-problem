# -*- coding: utf-8 -*-

def check_palindrome(l):
    l_1 = str(l)   #将数字转换为字符串
    p = l_1[::-1]
    if p == l_1:
        print("palindrome")
    else:
        print(p)