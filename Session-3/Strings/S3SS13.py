def isReverse(word1, word2):
    i = 0
    j = len(word2)
    flag = False
    if(len(word1)!=len(word2)):
        return False
    while(j>=0 and i<= len(word1)-1):
        if(word1[i] != word2[j-1]):
            return False
        i+=1
        j-=1
    return True

print(isReverse('apple', 'elppa'))
print(isReverse('apple', 'elpia'))
