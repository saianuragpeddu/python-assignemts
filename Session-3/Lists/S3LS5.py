def addOddNumbers(numbers):
    return sum(i for i in numbers if i%2 == 1)

print(addOddNumbers([1, 4, 8, 9]))

