from sys import stdin

first_check = True
for i in stdin:
    if first_check:
        if i % 2 == 1:
            print("still running")
        first_check = False
    timer = i 