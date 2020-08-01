'''
    By: Bearded_Mucassi[lmucassi]
    Given a string, find the first non-repeating character in it and return its index.
    If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
'''

def first_uniqchar1(c):
    frequency = {}
    for i in c:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(c)):
        if frequency[c[i]] == 1:
            return i 
    return -1

print(first_uniqchar1('alphabet'))
print(first_uniqchar1('barbados'))
print(first_uniqchar1('crunchy'))
