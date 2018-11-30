import math
def calDistance(x1, y1, x2, y2):
       return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 -y1))

print(calDistance(1, 2, 3, 4))
print(calDistance(5, 4, 7, 8))
