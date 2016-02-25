#!/usr/bin/env python
# -*- coding: utf8 -*-
# Author: Geng Chao
# Filename: week1_problem2_zerods.py

def decode(aString, aList, times):
    '''
    The fuction is designed to decode the string you input
    based on the order list and times the list used
    input: a string code, a list representing order and a number on behalf of times
    output: right code
    '''
    
    while times > 0:
        rightCode = []
        for number in aList:
            rightCode.append(aString[number])
        aString = ''.join(rightCode)
        times -= 1
    return ''.join(rightCode)

if __name__ == '__main__':
    print 'Input:"ABC" [2,0,1] 2, Output:', decode("ABC",[2,0,1],2)
    print 'Input:"ABCD" [3,2,1,0] 1, Output:', decode("ABCD",[3,2,1,0],1)
    print 'Input:"12345" [3,1,2,4,0] 1, Output:', decode("12345",[3,1,2,4,0],1) 
