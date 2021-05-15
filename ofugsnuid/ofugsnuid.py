from sys import stdin

numbers = [int(x) for x in stdin.readlines()][1:]
for i in reversed(numbers):
    print(i)
