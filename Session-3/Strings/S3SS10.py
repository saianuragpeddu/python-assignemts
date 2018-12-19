def startEndVowels(word):
    vowels = 'AaEeIiOoUU'
    if (word == ''):
        return False
    elif (word[0] in vowels and word[-1] in vowels):
        return True
    else:
        return False


print(startEndVowels('apple'))
print(startEndVowels('google'))
