#!/usr/bin/env python
# -*- coding: utf8 -*-

def function(str):
    if (str == None or str == ""):
        return -1
    plalindrome = ""
    for i in range(len(str)):
        plalindrome = plalindrome + str[len(str) - i - 1]
    if(plalindrome == str):
        return "palindrome"
    return plalindrome

str = "abcd"
print function(str)
str = "Hi,this is apple!"
print function(str)
str = "BAT360"
print function(str)
str = "QWER!@#$123"
print function(str)
str = "1"
print function(str)
str = "ABCCBA"
print function(str)
