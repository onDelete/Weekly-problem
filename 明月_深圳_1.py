#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Compare(List_1, List_2):
    if len(List_1) < len(List_2):
        return 0
    else:
        for i in range(len(List_1) - len(List_2)):
            for j in range(len(List_2)):
                if List_1[i+j] == List_2[j]:
                    if j == len(List_2)-1:
                        return 1
                    else:
                        pass
                else:
                    break
        return 0

if __name__ == '__main__':
    print Compare([0,1,2,3,4], [1,2])
    print Compare([0,1,2,3,1,2,3], [3,1,2])
    print Compare([1,0,2], [1,2])
            
