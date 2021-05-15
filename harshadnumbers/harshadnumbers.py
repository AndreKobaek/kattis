from sys import stdin


def sum_of_digits(x: int) -> int:
    sum = 0
    while x > 0:
        sum += x % 10
        x = int(x / 10)
    return sum


x = int(stdin.readlines()[0])

while x % sum_of_digits(x) != 0:
    x += 1
print(x)
