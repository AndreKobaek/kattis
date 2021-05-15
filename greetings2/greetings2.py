from sys import stdin

greeting = stdin.readlines()[0][:-1]
response_length = 2 * (len(greeting) - 2)
print("h", end="")
for _ in range(response_length):
    print("e", end="")
print("y")
