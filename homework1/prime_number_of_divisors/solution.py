def sum_of_divisors(n):
	result = 0
	for i in range(1, n+1):
		if n % i == 0:
			result = result + i
	return result
def is_prime(n):
	return sum_of_divisors(n) == n+1 

def num_of_divisors(n):
	result=0
	for i in range(1,n+1):
		if n%i ==0:
			result = result+1
	return result

def prime_number_of_divisors(n):
	if is_prime(num_of_divisors(n)):
		return True
	else:
		return False