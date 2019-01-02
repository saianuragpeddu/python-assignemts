def convertVector(numbers):
    dict = {}
    count = 0
    for i in numbers:
        if i != 0:
            dict[count] = i
        count+=1
    return dict

print(convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))
