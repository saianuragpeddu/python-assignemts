def sqrt_approx(num):
    i = 0
    minsq = 0
    maxsq = 0
    while i <= num:
        if i * i <= num:
            minsq = i
        if i * i >= num:
            maxsq = i
            break
        i = i + 1
    return minsq, maxsq


for i in range(0, 26):
    print(i, sqrt_approx(i))
