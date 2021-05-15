from sys import stdin

lst = [int(x) for x in stdin.readlines()[0].split()]
if lst[0] >= lst[2] + 2 and lst[1] >= lst[3] + 2:
    print(1)
else:
    print(0)
