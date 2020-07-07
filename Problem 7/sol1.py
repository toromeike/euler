from math import log
from math import ceil

def primes_up_to(n):
    '''
    Lists the primes smaller or equal than n
    '''
    n = ceil(n)
    not_prime = []
    primes = []
    for i in range(2, (n+1) ):
        if i not in not_prime:
            not_prime = not_prime + [i*k for k in range(2,(n//i + 1))]
            primes.append(i)
    return primes

#By Rossers theorem the nth prime is smaller than n*log(n) + n*log(log(n))

x = 10001
n = x * log(x) + x * log(log(x))
print(primes_up_to(n)[x-1])