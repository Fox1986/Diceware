import random

x = raw_input("Wie viele Woerter brauchen Sie? ")
x = int(x)
y = 0

while y < x:
    z = 0
    Wort = []
    while z < 5:
        Wort.append(random.randint(1, 6))
        z = z + 1
    y = y + 1
    print Wort
raw_input("Beliebige Taste zum beenden")
