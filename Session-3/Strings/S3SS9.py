def capitalizeVowels(word):
    result = ""
    vowels = 'AaEeIiOoUu'
    for i in word:
        if (i in vowels):
            result += i.upper()
        else:
            result +=i
    return result


print(capitalizeVowels('apple'))
