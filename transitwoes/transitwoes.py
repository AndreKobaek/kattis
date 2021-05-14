from sys import stdin

times = list()
for i in stdin:
    times.append([int(x) for x in i.split()])

s, t, n = times[0]
d0 = times[1][0]
ds = times[1][1:]
bs = times[2]
cs = times[3]

time = s + d0
for index in range(n):
    interval = cs[index]
    if time == 0:
        time += bs[index]
    else:
        while time > interval:
            interval += interval
        time = max(time, interval) + bs[index] + ds[index]

if time < t:
    print("yes")
else:
    print("no")
