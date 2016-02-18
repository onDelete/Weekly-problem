#!/usr/bin/env python
#FileName:hsm225_1.py

'''
practice: help a programmer to buy gift as much as possbile.
'''

def buy_gift(money, Gift_List):
	Gift_List.sort()
	Buy_Gift_List = []
	for i in Gift_List:
		if money - i >= 0:
			Buy_Gift_List.append(i)
			money -= i
	return len(Buy_Gift_List)

if __name__ == '__main__':
	money = int(raw_input("Please enter the money>>>"))
	Gift_List = []
	gift = raw_input("Please enter the gift>>>")
	while gift != '':
		if gift.isdigit():
			Gift_List.append(int(gift))
		else:
			pass
		gift = raw_input("Please enter the gift>>>")
	print "\n*Budget X: %d\t Gift_List: %r" % (money, Gift_List)	
	print "Output: %d" % buy_gift(money, Gift_List)
