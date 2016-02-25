#!/usr/bin/env python
# -*- coding: utf8 -*-
# Author: Geng Chao
# Filename: week1_1_zerods.py

def stringReverse():
    '''
    input: a string
    output: if the string is palindrome, then print 'palindrome'
            else: print the reversed string
    '''
    while True:
        reversedString = []
        aString = input('input:')
        if not isinstance(aString, str):
            print 'Invalid input, please try again!'
            continue
        length = len(aString)
        for i in range(length - 1, -1, -1):
            reversedString.append(aString[i])
        if ''.join(reversedString) == aString:
            print 'palindrome!'
            continue
        else: print ''.join(reversedString)

if __name__ == '__main__':
    stringReverse()
