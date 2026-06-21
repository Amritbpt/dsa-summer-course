import math

p1 = (0, 0)
p2 = (3, 4)

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(distance(p1, p2))