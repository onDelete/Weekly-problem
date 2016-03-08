x=1
list=[3,2,1]

def function(x,list):
	list=sorted(list)
	total=0
	count=0
	for i in list:
		total+=i
		if total>x:
			break
		count+=1
	return count

# print function(3,list)
# n=10
# def fuct(n):
# 	list=range(1,n+1)
# 	for i in list:
# 		if i mod 3 ==0:
# 			list.pop(i)

def funct(x):
	lst1=range(x+1)[1:]
	print lst1
	i=0
	while True:
		i+=2
		print "i=%s"%i
		print lst1[i]
		lst1.pop(i)
		print "lst=%s"%lst1
		if i+3>len(lst1):
			i-=len(lst1)
		if len(lst1)==1:
			break
	return lst1[0]

print funct(10)