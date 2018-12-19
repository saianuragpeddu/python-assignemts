def transpose(matrix):
    return map(list, zip(*matrix))

M = [[1,2,3], [4,5,6]]
print(transpose(M))
