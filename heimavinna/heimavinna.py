from sys import stdin

tasks = stdin.readlines()[0][:-1].split(";")
to_do = 0
for i in tasks:
    if len(i.split("-")) == 1:
        to_do += 1
    else:
        to_do += int(i.split("-")[1]) - int(i.split("-")[0]) + 1
print(to_do)
