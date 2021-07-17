from random import *

    
while True:
    print("--- New game ---")
    
    print("\nChoose a level from 1 to 6")
    level=input("Level : ")
    while level not in ["1","2","3","4","5","6"]:
        print("\nChoose a valid level")
        print("Choose a level from 1 to 6")
        level=input("\nLevel : ")
    level=int(level)
    if level==1:
        target=randrange(20,31)
    elif level==2:
        target=randrange(40,61)
    elif level==3:
        target=randrange(70,91)
    elif level==4:
        target=randrange(100,121)
    elif level==5:
        target=randrange(130,181)
    elif level==6:
        target=randrange(200,211)
    else:
        break

    a=1
    your_score=0
    print("\nComputer score =",target)
    while a==1:
        you=input("You : ")
        while you not in ["1","2","3","4","5","6"]:
            print("Invalid number")
            print("Choose a number from 1 to 6")
            you=input("You : ")
        you=int(you)
        com=randrange(1,7)
        print("Com :",com)
        if you==com:
            print("Out")
            print("Your Score=",your_score)
            if your_score<target:
                print("Computer Wins\n\n")
            elif your_score==target:
                print("Tie\n\n")
                a=2
            your_score=0
            a=2
        else:
            your_score+=you
            print("Your Score=",your_score)

            if your_score>target:
                
                print("You Wins\n\n")
                your_score=0
                a=2
                
        
            

