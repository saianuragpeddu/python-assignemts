def countLetters(word):
    letter = []
    count = []
    for c in sorted(word):
        if c not in letter:
            letter.append(c)
            count.append(1)
        else:
            count[-1] +=1
    return zip(letter, count)

print(countLetters('google'))
