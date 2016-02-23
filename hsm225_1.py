#!/usr/bin/env python

def StringReversal(s):
	s_reversal = s[::-1]
	if s[:len(s)/2] == s_reversal[:len(s_reversal)/2]:
		print "Output: palindrome"
	else:
		print "Output: %s" % s_reversal

if __name__ == '__main__':
	StringReversal('ABC')
	StringReversal('Hi, this is apple!')
	StringReversal('BAT360')
	StringReversal('QWER!@#$123')
	StringReversal('1')
	StringReversal('ABCCBA')
