from sys import stdin

for i in stdin:
    x, y, n = [int(x) for x in i.split()]
    for j in range(1, n+1):
        if j % x == 0 and j % y == 0:
            print("FizzBuzz")
        elif j % x == 0:
            print("Fizz")
        elif j % y == 0:
            print("Buzz")
        else:
            print(j)
