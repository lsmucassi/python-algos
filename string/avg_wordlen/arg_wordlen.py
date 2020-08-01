'''
    By: Bearded_Mucassi[lmucassi]
    For a given sentence, return the average word length. 
    Note: Remember to remove punctuation first.
'''

def avg_wordlen(sentence):
    for sc in "!?',;.":
        sentence = sentence.replace(sc, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words), 2)

sentence1 = "Algorithms that require you to apply some simple calculations using strings are very common"
sentence2 = "I have seen this problem presented in many different ways but it usually is the starting point for more complex requests."
print(avg_wordlen(sentence1))
print(avg_wordlen(sentence2))
