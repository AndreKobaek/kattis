from sys import stdin

first_check = True
second_check = True
area = 0
for i in stdin:
    if first_check:
        width = int(i)
        first_check = False
        continue
    if second_check:
        second_check = False
        continue
    else:
        lst = [int(x) for x in i.split()]
        area += lst[0] * lst[1]
print(int(area / width))
