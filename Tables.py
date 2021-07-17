while True:
    print("\nYour Tables:")
    a = int(input(" OF:"))
    b = int(input(" TILL:"))
    c = 1
    while c <= b:
        d = a * c
        print(c, "x", a, '=', d)
        c = c + 1
