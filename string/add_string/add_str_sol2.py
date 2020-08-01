'''
    By: Bearded_Mucassi[lmucassi]
    Given a string of length one, the ord() function returns an integer representing the Unicode code point of the character 
    when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.
'''
str1 = '354'
str2 = '1836'

#first posible solution 

def add_str2(str1, str2):
    eval(str1) + eval(str2)
    return str(eval(str1) + eval(str2))

print(add_str1(str1, str2))

