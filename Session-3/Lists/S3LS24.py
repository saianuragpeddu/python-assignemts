def getSumOfFirstDigit(num):
    a = 0
    for x in num:
        temp = str(x)
        a += int(temp[0])
    return a

print(getSumOfFirstDigit([12,23,34,45,56]))


    
