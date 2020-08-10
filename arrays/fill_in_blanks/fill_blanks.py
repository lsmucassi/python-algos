''' 
    By: Bearded_Mucassi[lsmucassi]
    Given an array containing None values 
    fill in the None values with most recent
    non None value in the array
'''

arr = [1, None, 2, None, 3, 56, 7, 0, 87, 786, 5, None]

def fill_blanks(array):
    valid = 0
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

print(fill_blanks(arr))
