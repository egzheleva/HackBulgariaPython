def sum_of_divisors(n):
	result = n
	for i in range(1,n):
		if n%i == 0:
			result=result+i
	return result

def is_prime(n):
	return sum_of_divisors(n) == n+1 