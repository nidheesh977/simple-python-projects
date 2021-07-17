from random import *
print("Select 1 for Snake\n       2 for Water\n       3 for Gun.")
player1=0
player2=0
Com=0
You=0
def player_1():
    global player1
    player1=input("Your turn : ")
    while player1 not in ["1","2","3"]:
        print("Invalid input ")
        player1=input("Your turn : ")
    player1=int(player1) 
    if player1==1:
        print("\nYou - Snake")

    elif player1==2:
        print("\nYou - Water")

    elif player1==3:
        print("\nYou - Gun")
    
    
def player_2():
    global player2
    player2=randrange(1,4)
    if player2==1:
        print("Com - Snake")

    elif player2==2:
        print("Com - Water")

    elif player2==3:
        print("Com - Gun")

def winner():
    global Com
    global You
    if player1==1 and player2==3:
        print("\nCom Win")
        Com+=1

    elif player1==2 and player2==1:
        print("\nCom Win")
        Com+=1

    elif player1==3 and player2==2:
        print("\nCom Win")
        Com+=1
        
    elif player1==player2:
        print("\nTie")
        
    else:
        print("\nYou Win")
        You+=1

def score():
    print("\nYour score  -",You)
    print("Com score -",Com,"\n")


def play_game():
    player_1()
    player_2()
    winner()
    score()

while True:
    play_game()


    
