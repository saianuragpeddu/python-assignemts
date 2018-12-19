def removeFirstAndLast(numbers):
    new = list(numbers)
    new.pop(0)
    if not new:
        return new
    new.pop()
    return new

print(removeFirstAndLast([1,4,3]))
