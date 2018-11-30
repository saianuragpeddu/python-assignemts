def getSumOfLastDigits(numList):
    return sum(x % 10 for x in numList)

print(getSumOfLastDigits([13,234,543]))
print(getSumOfLastDigits([23,43,564]))
