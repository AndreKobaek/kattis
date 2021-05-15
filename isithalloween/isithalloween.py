from sys import stdin

date = stdin.readlines()[0][:-1]

if date == "DEC 25" or date == "OCT 31":
    print("yup")
else:
    print("nope")
