def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    else:
        return True


print(isPrime(97))
print(isPrime(4))
print(isPrime(-2))
print(isPrime(50))
