def isPalindrome(word):
    word = str(word)
    if (word == ""):
        return False
    word = word.lower()
    rev = word[::-1]
    if rev == word:
        return True
    else:
        return False

print(isPalindrome('121'))
print(isPalindrome('Never'))
print(isPalindrome('Racecar'))
print(isPalindrome('level'))
