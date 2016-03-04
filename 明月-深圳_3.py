#!/usr/bin/env python
# -*- coding:utf-8 -*-

def SORT(List):
    for i in range(len(List)):
        for j in range(len(List)-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
            else:
                pass
    return List
    
if __name__ == '__main__':
    print SORT([3, 2, 1])
    print SORT([1, 5, 4, 6, 7])
    print SORT([0, 2, 4, 5, 7])
    print SORT([1])
