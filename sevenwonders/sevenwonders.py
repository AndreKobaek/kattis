from sys import stdin

cards = stdin.readlines()[0][:-1]

ts = 0
cs = 0
gs = 0

for a in cards:
    if a == "T":
        ts += 1
    elif a == "C":
        cs += 1
    elif a == "G":
        gs += 1
print(ts ** 2 + cs ** 2 + gs ** 2 + min(ts, cs, gs) * 7)
