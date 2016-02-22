#!/usr/bin/evn python
# coding:utf-8

if __name__ == '__main__':
    list = [] #商品列表
    money = int(raw_input("Your budget is:\n>").strip())
    shop_number = int(raw_input("How many commodities in stores?\n>").strip())
    x = 1
    while True:
    	if x <= shop_number:
    		shop_price = int(raw_input("Please input the price：\nNo.%d>"%x).strip())
    		list.append(shop_price)
    		x += 1
    	else:
    		break  
    def gifts(money,list):
    	list.sort()
    	gift = []
    	for i in list:
    		if money - i >= 0:
    			gift.append(i)
    			money -= i
    			i += 1
    		else :
    			pass
    	return len(gift)
    print "Your budget is:%r."%money
    print "List of goods：%r"%list
    print "You can buy the number of gifts:%d"%gifts(money,list)
