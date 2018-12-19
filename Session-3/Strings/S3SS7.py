def countVowels(word):
    count = 0
    vowels = 'AaEeIiOoUu'
    for i in word:
        if (i in vowels):
            count +=1
    return  count

print(countVowels('water'))
