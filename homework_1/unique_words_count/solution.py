def member(word,lst):
	for i in range(len(lst)):
		if word ==  lst[i]:
			return True
			break
	return False
def unique_words_count(arr):
	result= []
	for i in arr:
		if member(i, result) == False:
			result.append(i)
	return len(result)