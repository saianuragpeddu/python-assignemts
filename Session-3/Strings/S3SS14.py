def startWithVowel(word):
    vowels = "aeuioy"
    i = 0
    index = -1
    length = len(word)-1
    while(i <= length):
        if(word[i] in vowels):
            index = i
            break
        i+=1
    if(index == -1):
        return 'No vowel'
    else:
        return word[index:]

print(startWithVowel('paple'))
print(startWithVowel('banana'))
