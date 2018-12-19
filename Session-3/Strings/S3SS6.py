def getChar(word, pos):
    if (pos > len(word)):
        return "Invalid Range"
    else:
        return word[pos]


print(getChar("google", 4))
print(getChar("yahoo!", 10))
