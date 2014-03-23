def sum_of_divisors(n):
	result = 0
	for i in range(1, n+1):
		if n % i == 0:
			result = result + i
	return result
def is_perfect(n):
	return n == sum_of_divisors(n)