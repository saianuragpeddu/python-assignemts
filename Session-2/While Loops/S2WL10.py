def piApprox(num):
    pi = 4.0
    k = 1.0
    est = 1.0
    while 1<num:           
        k+=2
        est=est-(1/k)+1/(k+2)
        num=num-1
        k+=2
    return pi*est

print(piApprox(10))
