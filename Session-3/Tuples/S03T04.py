def commonElements(first, second):
    return tuple((sorted(set(first) & set(second))))

print(commonElements((1, 2, 3), (2, 5, 1)))
print(commonElements((1, 2, 3, 'p', 'n'), (2, 5 ,1, 'p')))
