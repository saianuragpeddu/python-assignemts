def addNumbers(start, end):
    total = 0
    while start <= end:
        total+=start
        start+=1
    return total

print(addNumbers(2, 5))
