def reverse_string(s):
    s2 = ''
    for i in range(len(s)):
        s2 = s2 + s[-i - 1]
    return s2

s = input("Enter a string: ")
s2 = reverse_string(s)

if s==s2:
    print('palindrome')
else:
    print(reverse_string(s))    
    
