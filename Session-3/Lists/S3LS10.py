def getMinNumber(numbers):
    if numbers == []:
        return 'N.A'
    else:
        return min(numbers)

print(getMinNumber([12,4,2,13]))
print(getMinNumber([]))
