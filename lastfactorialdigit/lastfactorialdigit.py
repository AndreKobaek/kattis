from sys import stdin
first_check = True
for i in stdin:
    if first_check:
        first_check = False
        continue
    else:
        n = int(i)
        if n <= 2:
            print(n)
        elif n == 3:
            print(6)
        elif n == 4:
            print(4)
        else:
            print(0)
