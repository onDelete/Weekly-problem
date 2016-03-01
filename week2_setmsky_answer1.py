#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# author: setm

def find_max_char_num(raw_str):
	# raw_str = raw_input('Enter your string: ')
	print 'input:', raw_str, "\t output:",
	# 
	#if 'O' not in raw_str or 'X' not in raw_str:
		#print '0'
		#return;
	index = 0
	# 
	max = 0
	o_sign = 0
	# loop raw_str
	for rs in raw_str:
		if rs == 'O':
			index = index + 1
		elif rs == 'X':
			if max < (index + o_sign):
				max = index + o_sign
			
			o_sign = index
			index = 0
	if index != len(raw_str):
		if max < (index + o_sign):
			max = index + o_sign
	print max 
	
def test_answer1():
	find_max_char_num('OXO')
	find_max_char_num('OXOOXOXXOOOXO')
	find_max_char_num('OOXOOOXOXO')
	find_max_char_num('XOOXOOOXOXO')
	find_max_char_num('OOOOOOOOOO')
	find_max_char_num('XXX')
	find_max_char_num('XOXOXtttss')
	find_max_char_num('OXXOOOXOOOXOOXXOXOOOOXXOXXXOXXOXXO')

if __name__ == '__main__':
	test_answer1()
	"""
	answer print:
	input: OXO 				output: 2
	input: OXOOXOXXOOOXO 	output: 4
	input: OOXOOOXOXO 		output: 5
	input: XOOXOOOXOXO 		output: 5
	input: OOOOOOOOOO 		output: 0
	input: XXX 				output: 0
	input: OXXOOOXOOOXOOXXOXOOOOXXOXXXOXXOXXO 	 output: 6
	"""
