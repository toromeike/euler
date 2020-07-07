from math import sqrt
from math import ceil

def is_prime(n):
    r = 1
    d = 2
    if n == 2:
        return True
    while r != 0 and d <= ceil(sqrt(n)):
        r = n % d
        d = d + 1
    return r != 0

def nth_prime(n):
    count = 1
    p = 2
    if n == 1:
        return p
    while count < n:
        p = p + 1
        if is_prime(p):
            count = count + 1
    return p