from time import sleep
def sand_clock():
    n=13
    s=1
    for i in range(7):
        print(s*" ",n*"#")
        n-=2
        s+=1
    n=1
    s=7
    for i in range(7):
        print(s*" ",n*"#")
        n+=2
        s-=1
    while True:
        input()
sand_clock()
