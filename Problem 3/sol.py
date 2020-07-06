from math import floor
from math import sqrt
            
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
    return(divs)

def prime_factors(n):
    '''
    Lists all proper prime factors of an integer n >= 3. 
    Returns an empty list for a prime.
    '''
    divs = divisors(n)
    divs.sort(reverse = True)
    p_factors = []
    if divs == [1]:
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
    return(p_factors)

x = 600851475143
print(max(prime_factors(x)))