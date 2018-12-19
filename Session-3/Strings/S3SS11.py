def removeVowels(word):
    vowels = 'AaEeIiOoUu'
    result = ""
    for i in word:
        if (i not in vowels):
            result +=i
    return result

print(removeVowels('apple'))
print(removeVowels('banana'))
