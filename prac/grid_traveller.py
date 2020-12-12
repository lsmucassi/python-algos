'''
Say that you are a traveller on a 2D grid. You begin in the top-left corner 
and your goal is to travel to the bottom-right corner.
You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Write a function `grid_traveller(m, n)` that calculates the number of ways.
'''

# memorization
def grid_traveller(m, n, memo={}):

    key = str(m) + ',' + str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = grid_traveller(m -1, n, memo) + grid_traveller(m, n -1, memo)
    return memo[key]

print(grid_traveller(1,1))
print(grid_traveller(2,3))
print(grid_traveller(3,2))
print(grid_traveller(3,3))
print(grid_traveller(18,18))
