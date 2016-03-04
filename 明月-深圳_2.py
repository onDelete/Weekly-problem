#!/usr/bin/env python
#! -*- coding:utf-8 -*-

def left():
    global i, j, num
    global List
    if List[i][j-1] == 'O':
        num += 1
        
def right():
    global i, j, num
    global List
    if List[i][j+1] == 'O':
        num += 1   
        
def up():
    global i, j, num
    global List
    if List[i-1][j] == 'O':
        num += 1           

def down():
    global i, j, num
    global List
    if List[i+1][j] == 'O':
        num += 1
def main(string, n):
    global i, j, num
    global List
    List = []
    NumList = []
    for seq in range(0, len(string), n):
        List.append(string[seq:seq+n])
    for i in range(len(List)):
        for j in range(n):
            num = 0
            if List[i][j] == 'X':
                if i == 0 and j ==0:
                    right()
                    down()
                elif i ==0 and j == n-1:
                    left()
                    down()
                elif i == 0:
                    left()
                    right()
                    down()
                elif i == len(List)-1 and j == 0:
                    up()
                    right()
                elif i == len(List)-1 and j == n-1:
                    up()
                    left()
                elif i == len(List)-1:
                    up()
                    left()
                    right()
                elif j == 0:
                    up()
                    down()
                    right()
                elif j == n-1:
                    up()
                    down()
                    left()
                else:
                    right()
                    left()
                    up()
                    down()
            NumList.append(num)
    return max(NumList)
    
if __name__ == '__main__':
    print main('OXOOOXOXOXOXXOX', 5)
    print main('XOOXOOOOOOXOOXOXXXOX', 5)
    print main('OXOOXOXOOOOXOOOXOXOXOOOOOXOOOXOOOOOXOOXOOXXOXOOOOOOXOXOOOOXOOOOOOXOOXOXXOXOXOXOX', 10)
