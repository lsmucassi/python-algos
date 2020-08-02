'''
    By: Bearded_Mucassi[lmucassi]
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    The string will only contain lowercase characters a-z.
'''

palin = 'radkar'

s = 'raddar'
def palindrome(s):
    x = ""
    diff = ord('a') - ord('A')
    for i in s:
        if ord(i) >= ord('a') and ord( 
    return s == s[::-1]

print(palindrome(s))
print(palindrome(palin))
