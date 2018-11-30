def addFirstAndLast(x):
    if len(x) == 0:
        return 0
    elif len(x) == 1:
        return x[0]
    return x[0] + x[-1]

print(addFirstAndLast([15,20,24]))
