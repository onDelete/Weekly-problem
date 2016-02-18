#!/usr/bin/env python
#FileName:hsm225_2.py

def Select_Last_One(N):
	if N == 0:
		return 0
	else:
		List = [i+1 for i in range(N)]
		while True:
			if len(List) > 3:
				NewList = List[3:]
				NewList.extend(List[0:2])
				List = NewList
			elif len(List) == 3:
				List = List[0:2]
			elif len(List) == 2:
				List = List[1:]
			else:
				return List[0]
				break

if __name__ == '__main__':
	N = int(raw_input("Please enter the number>>>"))
	print "\n*N=%d" % N
	print "Output: %d" % Select_Last_One(N)
