#!/usr/bin/python
# -*- coding: UTF-8 -*-

def function():
	n = int(raw_input("N = ").strip())
	m = 3
	j = 0
	for i in range(2,n+1):
		j = (m + j)%i
		print j
	return j+1

print "Output:%d"%function()
