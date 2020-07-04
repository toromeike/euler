from math import log10
from math import ceil

def ndigits(n):
    return(ceil(log10(n)))

n = 1000
digits = 1
fibs = [1,1]
counter = 2
while digits < n :
    fibs.append(fibs[-1] + fibs[-2])
    digits = ndigits(fibs[-1])
    counter = counter + 1
    
print(counter)
    