from sys import stdin

lst = [int(x) for x in stdin.readlines()[0].split()]
print(lst[0] * lst[1] * lst[2])
