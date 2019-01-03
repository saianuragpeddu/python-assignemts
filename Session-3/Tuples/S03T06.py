def shiftByTwo(*a):
    return a[len(a)-2:len(a)] + a[0:len(a)-2]

print(shiftByTwo(1,2,3,4,5,6))
print(shiftByTwo('a','b','c','d'))
print(shiftByTwo('a','b'))
