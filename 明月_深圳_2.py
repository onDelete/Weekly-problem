#!/usr/bin/env python
#! -*- coding:utf-8 -*-

def Compare(List_1, List_2):
    if len(List_1) < len(List_2):
        return 0
    else:
        n, i = 0, 0
        for item in List_2:
            if n >= len(List_1):
                return 0
            else:
                for entry in List_1[n:]:
                    if item == entry:
                        i += 1
                        break
                    else:
                        if i == len(List_1)-1:
                            return 0
                        else:
                            i += 1
                n = i
        return 1
    
if __name__ == '__main__':
    print Compare([1,3,2,4,3,5,6], [1,2,3,6])
    print Compare([1,2,1,1], [1,1,1])
    print Compare([1,2,1,2,0,1,2], [2,1,2,1])
    print Compare([3,2,1,0,7], [7,1,2,3])
    print Compare([1,3,5],[2])
    print Compare([1,3,5,7,9,8,6,4,2,0], [2,9,4,0])
    print Compare([1,3,5,7,9,8,6,4,2,0], [3,9,4,0])
