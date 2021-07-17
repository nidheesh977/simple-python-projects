import math

print("\n")

while True:
    d = 1
    b = int(input("\nSquare root till:"))
    f = '='
    e = "   "
    print("\nSquare root of:")
    while d <= b:
        c = math.sqrt(d)
        print(e, d, f, c)
        d = d + 1
