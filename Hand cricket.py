from random import *
while True:
    print("New game")
    a=1
    target=randrange(50,101)
    your_score=0
    print("Computer score =",target)
    while a==1:
        you=input("You : ")
        while you not in ["1","2","3","4","5","6"]:
            print("Invalid number. Choose a number from 1 to 6")
            you=input("You : ")
        you=int(you)
            
        com=randrange(1,7)
        print("Com :",com)
        if you==com:
            print("Out")
            print("Your Score=",your_score)
            if your_score<target:
                print("Computer Win\n\n")
            elif your_score==target:
                print("Tie\n\n")
                a=2
            your_score=0
            a=2
        else:
            your_score+=you
            print("Your Score=",your_score)

            if your_score>target:
                print("You Win\n\n")
                your_score=0
                a=2
                
        
            

