def isAnagram(w1, w2):
     w1 = sorted(w1.lower())
     w2 = sorted(w2.lower())
     if(w1==w2):
         return True
     return False

print(isAnagram('google', 'GOogel'))
print(isAnagram('anurag', 'Aragoo'))
