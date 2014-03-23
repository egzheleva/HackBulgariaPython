def calculate_coins(sum):
	dict = {}
	lst=[100,50,20,10,5,2,1]
	res=int(sum*100)
	for i in lst:
		n=res//i
		dict [i] = n
		res=res%i
		n=0
	return dict
