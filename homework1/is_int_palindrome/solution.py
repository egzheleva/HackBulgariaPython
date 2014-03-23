def is_int_palindrome(n):
	res=[]
	while n!=0:
		res.append(n%10)
		n=n//10
	tmp=res[::-1]
	return res==tmp

