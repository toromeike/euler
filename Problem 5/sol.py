from math import floor
from math import sqrt
from itertools import chain
from math import prod
            
def divisors(n):
    '''
    Lists all proper divisors (i.e. smaller than n) 
    of an integer n >= 2
    '''
    divs = [1]
    for d in range(2, floor(sqrt(n))):
        if n % d == 0:
            divs = divs + [d, n // d]
    if n % sqrt(n) == 0:
        divs.append(int(sqrt(n)))
    return divs

def prime_factors(n, itself = False):
    '''
    Lists all (proper if itself = True) prime factors of an integer n >= 3. 
    Returns an empty list for a prime if itself = True
    '''
    divs = divisors(n)
    divs.sort(reverse = True)
    p_factors = []
    if divs == [1]:
        if itself:
            return [n]
        else:
            return p_factors
    else:
        for i, d in enumerate(divs[:-1]):
            is_prime = True
            for d1 in divs[(i+1):-1]:
                if d % d1 == 0:
                    is_prime = False
                    break
            if is_prime:
                p_factors.append(d)
    return p_factors

def n_divides(n, d):
    '''
    Counts how many times a  factor divides a certain number. Returns
    0 if the number doesn't divide.
    '''
    k = 0
    r = 0
    while r == 0:
        r = n % d
        if r == 0:
            n = n // d
            k = k + 1
    return(k)
    
p_factors = [prime_factors(n, itself = True) for n in range(2,21)]
p_factors = list(set(list(chain(*p_factors))))

sol = 1
n_factors = []

for p in p_factors:
    n_factors.append(max([n_divides(n, p) for n in range(2,21)]))

print(sum([p**e for p,e in zip(p_factors, n_factors)]))