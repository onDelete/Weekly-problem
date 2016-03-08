def function1(str):
    assert len(str)>0
    if len(str) == 1:
        return True;
    else :
        return str[0] == str[-1] and function1(str[1:-1])
        
        

str = raw_input('input your string: ')
str1 = 'palindrome'
if function1(str) :
    print str1
else :
    print str[::-1];
