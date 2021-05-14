from sys import stdin
from math import cos, sin, radians

for i in stdin:
    if len(i.split()) == 1:
        continue
    else:
        v, theta, x, h1, h2 = [float(x) for x in i.split()]
        t = x / (v * cos(radians(theta)))
        y = v * t * sin(radians(theta)) - 0.5 * 9.81 * (t ** 2)
        if (y - 1) > h1 and (y + 1) < h2:
            print("Safe")
        else:
            print("Not Safe")
