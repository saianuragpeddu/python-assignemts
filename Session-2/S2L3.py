def generateNumber(start, end, step):
    if step > 0:
        return [i for i in range(start, end+1, step)]
    else:
        return [i for i in range(start, end-1, step)]

print(generateNumber(2, 10, 2))
print(generateNumber(15, 6, -2))
print(generateNumber(5, 3, -1))

