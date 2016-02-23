#!/usr/bin/env python

def BreakPassword(string, List, num):
	for i in range(num):
		new_string = ''
		for j in List:
			new_string += string[j]
		string = new_string
	print "Output: %s" % string

if __name__ == "__main__":
	BreakPassword('ABC', [2, 0, 1], 2)
	BreakPassword('ABCD', [3, 2, 1, 0], 1)
	BreakPassword('12345', [3, 1, 2, 4, 0], 1)
	BreakPassword('h?lunc', [1, 2, 3, 4, 5, 0], 2)
