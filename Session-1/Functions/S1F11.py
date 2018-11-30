def isEquilateral(x, y, z):
    if x < 0 or y < 0 or z < 0:
        return False
    return x == y and y == z

print(isEquilateral(2, 3, 4))
print(isEquilateral(5, 5, 5))
