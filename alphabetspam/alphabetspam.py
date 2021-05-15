from sys import stdin

lowercase = 0
uppercase = 0
whitespace = 0

charlist = stdin.readlines()[0][:-1]

for c in charlist:
    i = ord(c)
    if i == 95:
        whitespace += 1
    elif i >= 65 and i <= 90:
        uppercase += 1
    elif i >= 97 and i <= 122:
        lowercase += 1
print("{:.15f}".format(whitespace / len(charlist)))
print("{:.15f}".format(lowercase / len(charlist)))
print("{:.15f}".format(uppercase / len(charlist)))
symbols = (len(charlist) - whitespace - lowercase - uppercase) / len(charlist)
symbols_str = "{:.15f}".format(symbols)
print(symbols_str)
