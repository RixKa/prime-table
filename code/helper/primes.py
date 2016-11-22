import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return n>1


def get_n_primes(n):
    num = 1
    primes = [2]

    while len(primes) < n:
        num += 2
        if is_prime(num): primes.append(num)
    return primes
