def countOddNumbers(numbers):
    return (numbers[0]%2) + countOddNumbers(numbers[1:]) if numbers else 0

print(countOddNumbers([1, 4, 8, 9]))
print(countOddNumbers([1, 20, 3]))
print(countOddNumbers([]))
