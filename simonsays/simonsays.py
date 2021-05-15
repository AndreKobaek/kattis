from sys import stdin

skip_first = True
for i in stdin:
    if skip_first:
        skip_first = False
        continue
    command = i[:-1].split("Simon says")
    if len(command) == 2:
        print(command[1])
