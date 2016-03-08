# -*- coding: utf-8 -*-

def function(list_a, list_b):
    length_a = len(list_a)
    length_b = len(list_b)
    if length_a > length_b:
        for i in range(length_a - length_b + 1):
            if list_a[i:i+length_b] == list_b:
                return 1
        return 0
    else:
        return 0
