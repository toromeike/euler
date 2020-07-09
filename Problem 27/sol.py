from math import ceil
from math import sqrt
from itertools import product

def is_prime(n):
    r = 1
    d = 2
    if n < 0:
        return False
    if n == 2:
        return True
    while r != 0 and d <= ceil(sqrt(n)):
        r = n % d
        d = d + 1
    return r != 0

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

up_to = 1000
coefs = primes_up_to(up_to)

#First thoughts: b has to be prime and positive, else n^2+an+b is not prime
#for n = 0. Also a != b and a has to be odd (else the polynomial 
#is not prime for n = 0 or n = 1)

pols = [(a, b) for a, b in product(list(range(-999, 1000, 2)), coefs) 
        if a != b]

max_pair = (0, 0)
max_prime_seq = 0

for pair in pols:
    n = 0
    a, b = pair
    is_value_prime = is_prime(n**2 + a * n + b)
    while is_value_prime:
        n = n + 1
        is_value_prime = is_prime(n**2 + a * n + b)
    if n > max_prime_seq:
        max_pair = (a, b)
        max_prime_seq = n
        
a, b = max_pair
print(a*b)