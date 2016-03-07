#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

# author: setm

def kmp_search(txt, pattern):
	txt_len = len(txt)
	pattern_len = len(pattern)
	dfa = []
	j = 0
	# create dfa
	dfa.append(0)
	for i in range(1, pattern_len):
		while j > 0 and pattern[j] != pattern[i]:
			j = dfa[j - 1]
		if pattern[i] == pattern[j]:
			j = j + 1
		dfa.append(j)
	# reset
	j = 0
	for i in range(0, txt_len):
		while j > 0 and txt[i] != pattern[j]:
			j = dfa[j - 1]
		if txt[i] == pattern[j]:
			j = j + 1
		if j == pattern_len:
			return 1
	return 0


def is_include(list1, list2):
	print 'input: txt ', list1, '||', list2, ' output:',
	if list1 == None or list2 == None:
		return 0;
	len1 = len(list1)
	len2 = len(list2)
	i = 0 
	j = 0
	if len1 < len2:
		return 0
	elif len1 == len2:
		for i in range(len1):
			#for j in range(len2):
			if list1[i] != list2[i]:
				return 0
		return 1
	else:
		return kmp_search(list1, list2)

def test_run1():
	print is_include([0,1,2,3,4],[1,2])
	print is_include([0,1,2,3,1,2,3],[3,1,2])
	print is_include([1,0,2],[1,0,2])
	print is_include([1,0,2],[1,2])
	print is_include([8,0,1,3,2],[1,0,2])

def is_make_arry(list1, list2):
	print 'input: txt ', list1, '||', list2, ' output:',
	if list1 == None or list2 == None:
		return 0;
	len1 = len(list1)
	len2 = len(list2)
	j = 0
	if len1 < len2:
		return 0
	else:
		for i in range(len1):
			if list1[i] == list2[j]:
				j = j + 1
			if j == len2:
				return 1
		return 0

def test_run2():
	print is_make_arry([1,3,2,4,3,5,6],[1,2,3,6])
	print is_make_arry([1,2,1,1],[1,1,1])
	print is_make_arry([1,2,1,2,0,1,2],[2,1,2,1])
	print is_make_arry([3,2,1,0,7],[7,1,2,3])
	print is_make_arry([1,3,5],[2])

if __name__ == '__main__':
	print 'question1:'
	print '----------------------------------'
	test_run1()
	print
	print 'question2:'
	print '----------------------------------'
	test_run2()

