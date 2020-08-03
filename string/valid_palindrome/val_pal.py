'''
    By: Bearded_Mucassi[lmucassi]
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    The string will only contain lowercase characters a-z.
'''

palin = 'radkar'

s = 'A Man, a Plan, a Canal: Panama'

def palindrome(s):
    x = ""
    diff = ord('a') - ord('A')
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z') or ord(i) >= ord("0") and ord(i) <= ord("9"):
            x += i
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            i = chr(diff+ord(i))
            x += i
    return x == x[::-1]

print(palindrome(s))
print(palindrome(palin))
