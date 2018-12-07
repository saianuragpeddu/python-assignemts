def addEvenNumbers(start, end):
    return sum(i for i in range(start, end + 1) if i % 2 == 0)

print(addEvenNumbers(3, 7))
print(addEvenNumbers(5, 12))
