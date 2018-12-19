def skipVowels(word):
    novowels = ''
    for ch in word:
        if ch.lower() in 'aeiou': 
        	continue
        	novowels += ch
        novowels+=ch
    return novowels

print(skipVowels('hello'))
print(skipVowels('awaited'))

