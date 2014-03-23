def is_an_bn(word):
	temp1 = word [:len(word)//2]
	temp2 = word [len(word)//2:]
	if len(temp1) != len(temp2):
		return False
	for i in range ( len(temp1)):
		if temp1[i] != "a" or temp2[i]!= "b":
			return False
	return True