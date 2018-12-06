def quadratic(a, b, c):
   d = b**2 - 4*a*c
   if d < 0:
       return "This equation has 2 complex roots."
   elif d > 0:
       return "This equation has 2 real roots."
   else:  
       return "This equation has 1 real root."

print(quadratic(1,2,3))
print(quadratic(1,3,2))
print(quadratic(1,4,4))
