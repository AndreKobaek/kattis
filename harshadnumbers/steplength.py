def sum_of_digits(x: int) -> int:
    sum = 0
    while x > 0:
        sum += x % 10
        x = int(x / 10)
    return sum


counter = 0
max_counter = 0
for i in range(1, 100000000):
    if i % sum_of_digits(i) == 0:
        counter = 0
        continue
    counter += 1
    max_counter = max(counter, max_counter)
print(counter)
# 33
