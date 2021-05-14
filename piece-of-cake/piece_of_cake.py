from sys import stdin

for i in stdin:
    height = 4
    n, h, v = [int(x) for x in i.split()]
    print(max(n-h,h)*max(n-v,v)*4)