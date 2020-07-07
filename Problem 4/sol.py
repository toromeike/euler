def is_palindrome(x):
    '''
    Checks if an integer or string is a palindrome
    '''
    s = str(x)
    return s == s[::-1]


palindromes = []
#Rather inefficient looping. More efficient would be a zig-zag path through
#the outer product (999:100)^T * (999:100)
for i in range(999,99,-1):
    for j in range(999,99,-1):
        p = i*j
        if is_palindrome(p):
            palindromes.append(p)

print(max(palindromes))
        