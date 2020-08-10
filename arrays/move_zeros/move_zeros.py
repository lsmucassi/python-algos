'''
    By: Bearded_Mucassi[lsmucassi]
    Given an array nums, 
    write a function to move all zeroes to the end of it 
    while maintaining the relative order of the non-zero elements.
'''

arr1 = [0,1,5,9,7,3,0,5,9]
arr2 = [7,83,4,36,68,8,24,4,51,0,2,3,0,1,5,9,0,43,0]

def move_zeros(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

print(move_zeros(arr1))
print(move_zeros(arr2))
