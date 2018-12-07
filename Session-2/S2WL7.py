def doubleFactorial(num):
    product = 1 
    i = 0
    k = 0
    while k < num: 
       k = 2*i+1
       product *= k 
       i += 1
    return product

print(doubleFactorial(9))
