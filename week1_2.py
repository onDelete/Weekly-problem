#!/usr/bin/env python
# -*- coding: utf8 -*-


def function(str,list,N):
	for i in range(N):
		new_str = ""
		for j in list:
			new_str += str[j]

		str = new_str
	return str

if __name__ == '__main__':
	
	str = "ABC"
	list = [2,0,1]
	N = 2
	print function(str,list,N)

	str = "ABCD"
	list = [3,2,1,0]
	N = 1
	print function(str,list,N)

	str = "12345"
	list = [3,1,2,4,0]
	N = 1
	print function(str,list,N)
