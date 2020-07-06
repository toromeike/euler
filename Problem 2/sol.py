def fibs(n):
    '''
    For an integer n > 2, generates all fibonacci numbers 
    smaller or equal than n
    '''
    fibs = [1, 2]
    while fibs[-1] < n:
        fibs.append(fibs[-1]+ fibs[-2])
    return(fibs)
    
fib4mill = fibs(4e6)

#In the Fibonacci sequence every third number is divisible by 2

print(sum([fib for i, fib in enumerate(fib4mill) if (i-1) % 3 == 0]))