from sys import stdin

skip_first = True
for i in stdin:
    if skip_first:
        skip_first = False
        continue
    imported = 0
    turtle_series = [int(x) for x in i.split()][:-1]
    previous_year = turtle_series[-1]
    turtle_series = turtle_series[:-1]
    for x in reversed(turtle_series):
        imported += max(0, previous_year - 2 * x)
        previous_year = x
    print(imported)
