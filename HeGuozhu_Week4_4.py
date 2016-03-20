def findLargeSum0(arr):
    length = len(arr)
    sum,num= 0,0
    flag = True
    for i in range(0,length):
        sum = 0
        for j in range(i,length):
            sum += arr[j]
            if(sum == 0):
                if(j - i > num):
                    flag = False
                    num = j - i 
    if(flag == False):
        return num + 1
    else:
        return num 

def test():
    print("%d"%(findLargeSum0([2,-2])))
    print("%d"%(findLargeSum0([0,1,2,3,-1,-3,-1,5])))
    print("%d"%(findLargeSum0([0,1,2,3])))
    print("%d"%(findLargeSum0([1,1,1,1,1,1,-3,1,1,1,1,-4])))
    print("%d"%(findLargeSum0([1,-1,2,3,-2,-1])))

if __name__ == "__main__":
    test()
