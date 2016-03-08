
def decode(string,code,num):
	for j in range(num):
		output=[]
		for i in range(len(string)):
			attach=string[code[i]]
			output.append(attach)
		string=output
	return ''.join(output)

