def primeFactorization(num):
    result = []
    while(num != 1):
        for i in range(2, num):
            while(num % i == 0):
                result.append(i)
                num = num / i
                print(i)
                #i = 2
    return result

print(primeFactorization(20))
