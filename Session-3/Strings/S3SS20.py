def isInAlphabeticalOrder(word):
    sorted_word = "".join(sorted(word))
    if word == sorted_word:
        return True
    else:
        return False

print(isInAlphabeticalOrder('abczd'))
print(isInAlphabeticalOrder('abcdef'))
