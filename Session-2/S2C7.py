def isTriangle(x,y,z):
    if x + y <= z or y + z <= x or x + z <= y:
        return False
    else:
        return True

print(isTriangle(3,4,5))
print(isTriangle(1,2,3))

