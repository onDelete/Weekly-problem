#!/usr/bin/env python
# -*- coding: utf-8 -*-

def OX(string):
    InitList = list('X' + string + 'X')
    SecondList = list(enumerate(InitList, start=1))
    ThirdList = []
    for item in SecondList:
        if item[1] == 'X':
            ThirdList.append(item[0])
        else:
            pass
    if len(ThirdList) == len(SecondList) or len(ThirdList) - 2 == 0:
        return 0
    else:
        FourthList = []
        for i in range(len(ThirdList)-1):
            FourthList.append(ThirdList[i+1] - ThirdList[i] - 1)
        FifthList = []
        for j in range(len(FourthList)-1):
            FifthList.append(FourthList[j] + FourthList[j+1])
        return max(FifthList)
    
if __name__ == '__main__':
    print OX('OXO')
    print OX('OXOOXOXXOOOXO')
    print OX('OOXOOOXOXO')
    print OX('OOOOOOOOO')
    print OX('XXX')
    print OX('OXOOXOXOOOOXOOOXOXOXOOOOOXOOOXOOOOOXOOXOOXXOXOOOOOOXOXOOOOOOOXOOOOOOXOOXOXXOXOXOXOX')
