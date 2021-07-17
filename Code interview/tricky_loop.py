i = 1
def loop():
    global i
    print(i)

    if i != 100:
        i+=1
        loop()

loop()