def reverse(lst):
	res= lst[::-1]
	return res
def is_decreasing(seq):
	return seq==reverse(sorted(seq))

