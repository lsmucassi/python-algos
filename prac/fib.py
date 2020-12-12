'''
write a function `fib(n)` that takes in a number as an argument
The function should return the n-th number of the fibonacci sequence corresponding to the arg

the 1st and 2nd number of the sequence is 1
To generate the next number we sum the two previous numbers

n:      1, 2, 3, 4, 5, 6, 7, 8, 9 ....
fib:    1, 1, 2, 3, 5, 8, 13, 21, 34
'''

# memorization
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n -1, memo) + fib(n -2, memo)
    return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))