def removeCommonElements(first, second):
     return tuple((sorted(set(first) ^ set(second))))

print(removeCommonElements((1,2,3,4), (3,4,5,6)))
print(removeCommonElements(('b','a','c','d'), ('a','b','c')))
