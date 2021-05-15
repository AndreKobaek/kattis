from sys import stdin

sum = 1
skip_first = True
for i in stdin:
    if skip_first:
        skip_first = False
        continue
    sum += int(i) - 1
print(sum)
