from sys import stdin

skip_first = True

for i in stdin:
    if skip_first:
        skip_first = False
        continue
    sockets = [int(x) for x in i.split()]
    print(sum(sockets[1:]) - len(sockets[1:]) + 1)
