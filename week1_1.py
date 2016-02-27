#!/usr/bin/env python
# coding:utf-8
"""
给你一串字符串，你能否把它反转过来呢？不过，如果给你的字符串本身就是回文的话，你只需要输出"palindrome"即可！
"""


def function():
	strs = raw_input("The input:")
	new_strs = strs[::-1]
	if strs[:len(strs)/2] == new_strs[:len(new_strs)/2]:
		return "palindrome"
	else:
		return "Output:%r"%new_strs
	pass

print function()
