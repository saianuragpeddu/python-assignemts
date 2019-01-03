def det(M):
    return M[0][0]*M[1][1] - M[1][0]*M[0][1]

M = ((3,1), (5,2))
print(det(M))

M = ((8,1), (1,1))
print(det(M))
