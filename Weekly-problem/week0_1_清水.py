# coding = utf-8

def function(x , list):
    if x < 0 or list == None or list == [] : return '输入错误'
    num = 0
    sum = 0
    list.sort() #对list排序
    if list[0] > x: return 0
    for g in list:
        sum += p
        if sum > x:
            break
        num += 1
        
    return num


if __name__ == '__main__':
    x = 2
    list = [3,8,10]  
    print function(x, list)
