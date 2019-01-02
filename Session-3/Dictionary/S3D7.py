def countLetters(word):
    result = { }
    letters = ""
    for i in word:
        if i not in letters:
            letters += i
            result[i] = 0
    for i in word:
        if i in letters:
            result[i] += 1
    return result

print(countLetters("google"))
print(countLetters("apple"))

def countLetters2(word):
    dict = {}
    for i in set(word):
        b = word.count(i, 0, len(word))
        dict[i] = b
    return dict

print(countLetters("google"))
print(countLetters("apple"))
