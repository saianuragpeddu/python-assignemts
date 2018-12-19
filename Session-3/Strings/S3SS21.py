def isAllLettersUsed(word, required):
    l = list(word)
    for i in required:
        if i not in l:
            return False
    return True

print(isAllLettersUsed('apple','apple'))
print(isAllLettersUsed('learning python', 'apple'))
print(isAllLettersUsed('learning python', 'zebra'))
