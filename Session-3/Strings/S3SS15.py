def getCommonLetters(word1, word2):
   res = ""
   for letter in word1:
      if letter in word2:
         if letter not in res:
             res = res + letter
   res = ''.join(sorted(res))
   return res

print(getCommonLetters('apple', 'banana'))
print(getCommonLetters('sing', 'song'))
