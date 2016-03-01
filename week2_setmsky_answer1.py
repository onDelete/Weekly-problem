#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# author: setm
"""
解题思路整理如下:
对字符串OXXXOOOXOO
1. 计算O出现的次数,也就是X left边的O的出现次数
2. 对于XX 这样的,统一考虑为O为0的情况,也就是 left为0
3. 每次遇到X 计算上次O和这次O出现的和 最大值比较
"""
def find_max_char_num(raw_str):
	# raw_str = raw_input('Enter your string: ')
	print 'input:', raw_str, "\t output:",
	# 
	#if 'O' not in raw_str or 'X' not in raw_str:
		#print '0'
		#return;
	cur_count = 0
	# 
	max = 0
	old_count = 0
	# loop raw_str
	for rs in raw_str:
		if rs == 'O':
			cur_count = cur_count + 1
		elif rs == 'X':
			if max < (cur_count + old_count):
				max = cur_count + old_count
			
			old_count = cur_count
			cur_count = 0
	# 处理全部为OOOOOOOO的时候 跳过 . 同时用来处理 XOOOO 这样的结尾数据
	if cur_count != len(raw_str):
		if max < (cur_count + old_count):
			max = cur_count + old_count
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
