''' 
    By: beared_mucassi[lmucassi]
    Given an integer, return the integer with reversed digits.
    Note: The integer could be either positive or negative.
'''

def rev_int(x):
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])

num1 = -234
num2 = 345
print(rev_int(num1))
print(rev_int(num2))
