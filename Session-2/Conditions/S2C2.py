def isIsosceles(x, y, z):
    if x <= 0 or y <=0 or z <=0:
       return False
    if x == y:
       return True 
    if y == z:
       return True
    if x == z:
       return True
    else:
       return False


print(isIsosceles(-2, -2, 3))
print(isIsosceles(2, 3, 2))

def isIsosceles(x, y, z):
    if x <= 0 or y <=0 or z <=0:
       return False
    elif x == y or y == z or x == z:
       return True 
    else:
       return False

print(isIsosceles(-2, -2, 3))
print(isIsosceles(2, 3, 2))
