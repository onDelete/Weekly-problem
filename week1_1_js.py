def is_palindrome(inputStr):
	if len(inputStr)<=1:
		return True
 	else:
		return inputStr[0] == inputStr[-1] and is_palindrome(inputStr[1:-1])

def function(inputStr):
	if is_palindrome(inputStr):
		return "palindrome"
	else:
		return inputStr[::-1]

inputStr = raw_input()
print function(inputStr)
