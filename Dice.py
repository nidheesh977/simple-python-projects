from random import *
def dice():
    global a
    a=randrange(1,7)
    print(a)
dice()
while a==6:
    print(input("\nSame player :- Press Enter"))
    dice()
while True:
    print(input("\nNext player :- Press Enter"))
    dice()
    while a==6:
        print(input("\nSame player :- Press Enter"))
        dice()
