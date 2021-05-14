from sys import stdin

lst = stdin.readlines()[0].split()
length = len(lst)
if len(set(lst)) != length:
    print("no")
else:
    print("yes")
