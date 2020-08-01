'''
    By: Bearded_Mucassi[lmucassi]
    Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
    You must not use any built-in BigInteger library or convert the inputs to integer directly
    Notes:
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
'''
str1 = '354'
str2 = '1836'

#first posible solution 

def add_str1(str1, str2):
    eval(str1) + eval(str2)
    return str(eval(str1) + eval(str2))

print(add_str1(str1, str2))

