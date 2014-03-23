def member(elem,str):
	for i in str:
		if elem == i:
			return True
			break
	else:
		return False
def count_vowels(str):
	result=0
	for i in str.lower():
		if member(i,"aeouyi"):
			result+=1
	return result