def matrixDimensions(m):
    test = []
    a = len(m)
    for b in m:
        c = len(b)
        test.append(c)
        d = test[1:] == test[:-1]
    if d is False:
        return 'This is not a valid matrix.'
    else:
        return "This is a %dx%u matrix." % (a,c)


A = [[1,3], [-5, 6], [2,4]]
print(matrixDimensions(A))

B = [[1, 3, 3], [-9, 3]]
print(matrixDimensions(B))

C = [[1,2], [2,3,4], [2,3]]
print(matrixDimensions(C))



