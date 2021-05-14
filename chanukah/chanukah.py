from sys import stdin

for i in stdin:
    if len(i.split()) != 2:
        continue
    else:
        k, n = [int(x) for x in i.split()]
        sum = 0
        for j in range(n + 1):
            sum += j
        print(f"{k} {sum + n}")
