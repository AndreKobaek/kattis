from sys import stdin

sum = 0
lst = [int(x) for x in stdin.readlines()]
if lst[0] % 2 == 1:
    print("still running")
else:
    for i in range(2, lst[0]+2, 2):
        sum += lst[i]-lst[i-1]
    print(sum)