'''
    By: Bearded_Mucassi[lmucassi]
    Given a string, find the first non-repeating character in it and return its index.
    If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
'''
import collections

def first_uniqchar2(c):
    # build hash map of characters and count howmanytimes it appears
    count = collections.Counters(c)
    # gives back a dictionary with words occurrence count
    # Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})

    #find the index
    for iidx, ch in enumerate(len(c)):
        if count[ch] == 1:
            return idx
    return -1

print(first_uniqchar2('alphabet'))
print(first_uniqchar2('barbados'))
print(first_uniqchar2('crunchy'))
