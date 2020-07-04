from math import ceil
from math import sqrt

def sum_divs(n):
    s = 1
    if n == 2:
        return(1)
    if n == 1:
        return(0)
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            s = s + i + n//i
    if float.is_integer(sqrt(n)):
        s = s + ceil(sqrt(n))
    return(s)

l = 10000
ndivs = [sum_divs(n) for n in range(2,l)]

ndivs2 = ndivs + [sum_divs(n) for n in range(l, 2*ceil(l**(4/3))+1)]

amicables = []

for i, ndiv in enumerate(ndivs):
    if ndiv in ndivs2[:i]+ndivs2[i+1:]:
        amicables.append(i+2)

print(sum(amicables))