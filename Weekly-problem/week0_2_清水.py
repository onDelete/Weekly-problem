# coding = utf-8

def function(n):    
    if(n < 1): return 0
    arr = [1] * n  #创建n个1的list，‘1’代表还在座位，‘0’代表离开座位
    lenArr = n     
    
    index = 0
    count = 0
    
    while(lenArr > 1):
        if(arr[index] == 1):
            count += 1
            if(count == 3):
                count = 0
                arr[index] = 0   #数到第3个人离开
                lenArr -= 1      #人数减1
                
        index += 1            
        if(index == n):
            index = 0    #数到第n个后从头开始数
            

    return arr.index(1) + 1  #还剩1人没有离开，他的编号加1


if __name__ == '__main__':
    print function(5)
    print function(3)
    print function(6)
    print function(0)
    print function(500)
                
        
        
