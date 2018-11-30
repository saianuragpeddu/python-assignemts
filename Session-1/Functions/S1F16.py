def addOne(x):
        return x + 1
        
def useFunction(func, num): 
      return func(num) * func(num)

print(useFunction(addOne, 4))
print(useFunction(addOne, 0))
