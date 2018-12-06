def isScalene(x, y, z): 
    if x <= 0 or y <= 0 or z <= 0:
       return False
    elif x == y or y == z or x == z:
       return False
    else:
       return True

print(isScalene(2, 3, 2))
print(isScalene(3, 3, 3))
print(isScalene(4, 5, 6))
