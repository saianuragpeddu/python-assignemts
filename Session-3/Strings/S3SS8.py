def getVowels(word):
    res = []
    vowels = 'AaEeIiOoUU'
    for i in word:
        if (i in vowels):
            res +=i
    return res

print(getVowels("apple"))
print(getVowels("banana"))
