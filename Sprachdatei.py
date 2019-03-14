
f = open("Deutsch.txt")

Dict = ()
for line in f:
    line = str(line)
    Dict.__add__(line)

print Dict