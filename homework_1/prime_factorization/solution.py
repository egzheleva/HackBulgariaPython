def sum_of_divisors(n):
	result = n
	for i in range(1,n):
		if n%i == 0:
			result=result+i
	return result

def is_prime(n):
	return sum_of_divisors(n) == n+1 

def prime_range(n):
	result=[]
	for i in range(2,n+1):
		if is_prime(i):
			result.append(i)
	return result
def prime_factorization(n):
	result=[]
	tmp=0
	while n!=0:
		for i in prime_range(n):
			if is_prime(n):
				result.append((n,1))
				n=0
				break
			if n%i == 0:
				while n%i == 0 and n!=1:
					n=n//i
					tmp+=1
				result.append((i,tmp))
				tmp=0
	return result



