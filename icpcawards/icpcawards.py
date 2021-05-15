from sys import stdin

winners = list()
skip_first = True
for i in stdin:
    if skip_first:
        skip_first = False
        continue
    uni, team = i.split()
    if uni in winners or len(winners) >= 12:
        continue
    winners.append(uni)
    print(i[:-1])
