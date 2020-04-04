__author__ = 'Linda Mucassi'


arr = [5, 8, 4, 6, 9, 2, 7, 1]
n = 9

def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1
    
    print("not found")
    return False

if search(arr, n):
    print("found")
else:
    print("Not found")