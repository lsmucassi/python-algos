'''
Write a function `can_sum(target_sum, numbers)` that takes i a 
target_sum and an array of numbers as arguments.

The function should return a boolean indicating whether or not 
it is possible to generate the target_sum using numbers from
the array.

You mau use an element of the array as many times as needed,
You may assume that all input numbers are non-negatives.

can_sun(7, [5, 3, 4, 7]) --> True: 7 can be returned as is already a member and 3 + 4 sums to 7
can_sum(7, [2, 4]) --> False: no combination can sum to 7 from the given list
'''

def can_sum(target_sum, numbers, memo):
    if target_sum == 0: return True
    if target_sum < 0: return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers) == True:
            return True

    return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5,3,2,7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))