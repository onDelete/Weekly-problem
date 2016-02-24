#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

def ispalindrome(arg):
	length = len(arg)
	#  palindrome
	if length == 1:
		return True
	# 
	half = length / 2
	for i in range(1, half + 1):
		if arg[i-1] == arg[length - i]:
			continue
		else:
			return False
	else:
		return True


def _reversed(arg):
	length = len(arg)
	print 'in ', arg , '\t\t\t out: ',
	if arg == None or length < 0:
		print "cann't use empty string"
		return
	
	if ispalindrome(arg):
		print "palindrome"
		return
	
	#
	out = ''
	for x in range(0, length):
		out += arg[length - 1 - x]
	
	print out

def test_run():
	_reversed('ABC')
	_reversed('ABA')
	_reversed('testest')
	_reversed('Hi,this is apple!')
	_reversed('appleelppa')
	_reversed('BAT360')
	_reversed('12345654321')
	_reversed('QWER!@#$123')
	_reversed('1')
	_reversed('ABCCBA')

def decode_pass(arg, idx_a, size):
	length = len(arg)
	idx_len = len(idx_a)
	print 'pass ', arg, idx_a, size, '\t decode: ',
	if arg == None or length < 0:
		print "cann't use empty string"
		return
	if length != idx_len:
		print ''
		return
	
	tmp = list(arg)
	for i in range(size):
		f = [tmp[idx] for idx in idx_a]
		tmp[:] = f
	
	print ''.join(tmp)

if __name__ == '__main__':
	print 'Week1 Question1'
	test_run()
	print
	print '--------------------------'
	print 'Week1 Question2'
	decode_pass('ABC', [2,0,1], 2)
	decode_pass('ABCD', [3,2,1,0], 1)
	decode_pass('12345', [3,1,2,4,0], 1)

