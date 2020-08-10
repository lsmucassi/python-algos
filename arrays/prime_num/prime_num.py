'''
    By: Bearded_Mucassi[lsmucassi]
    Given k numbers which are less than n, 
    return the set of prime number among them
    Note: The task is to write a program to 
    print all Prime numbers in an Interval.
    Definition: A prime number is a natural number 
    greater than 1 that has no positive divisors other than 1 and itself.
'''

num = 35

def prime_num(num):
    prime_nums = []
    for num in range(num):
        if num > 1: # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:  # if the modulus == 0 is means that the number can be divided by a number preceding it
                    break
            else:
                prime_nums.append(num)
    return prime_nums

print(prime_num(num))
