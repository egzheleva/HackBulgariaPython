def sum_of_divisors(n):
    result = n
    for i in range(1, n):
        if n % i == 0:
            result = result + i
    return result


def is_prime(n):
    return sum_of_divisors(n) == n+1


def prime_range(n):
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result


def goldbach(n):
    result = []
    primes = prime_range(n)
    for i in range(len(primes)):
        for j in range(i , len(primes)):
            if primes[i] + primes[j] == n:
                result.append((primes[i], primes[j]))
    return result

