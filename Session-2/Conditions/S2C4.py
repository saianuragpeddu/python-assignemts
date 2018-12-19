def Fitness(a, b, c):
    msg = "Enter your score for the first station %a"
    if a >= 4 and b >= 4 and c >= 4 and a + b + c >= 13:
        return 'Gold'
    elif a >= 3 and b >= 3 and c >= 3 and a + b + c >= 10:
        return 'Silver'
    elif a >= 2 and b >= 2 and c >= 2 and a + b + c >= 7:
        return 'Pass'
    else:
        return 'Fail'


print(Fitness(2, 3, 1))
print(Fitness(2, 2, 3))
print(Fitness(3, 3, 5))
print(Fitness(5, 5, 7))




     
