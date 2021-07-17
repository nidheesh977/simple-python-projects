from random import *
print("Select 1 for Rock\n       2 for Paper\n       3 for Scissors.")
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
        print("\nYou - Rock")

    elif player1==2:
        print("\nYou - Paper")

    elif player1==3:
        print("\nYou - Scissors")
    
    
def player_2():
    global player2
    player2=randrange(1,4)
    if player2==1:
        print("Com - Rock")

    elif player2==2:
        print("Com - Paper")

    elif player2==3:
        print("Com - Scissor")

def winner():
    global Com
    global You
    if player1==1 and player2==2:
        print("\nCom Win")
        Com+=1

    elif player1==2 and player2==3:
        print("\nCom Win")
        Com+=1

    elif player1==3 and player2==1:
        print("\nCom Win")
        Com+=1

    elif player2==1 and player1==2:
        print("\nYou Win")
        You+=1

    elif player2==2 and player1==3:
        print("\nYou Win")
        You+=1

    elif player2==3 and player1==1:
        print("\nYou Win")
        You+=1

    

def Tie():
    if player1==player2:
        print("\nTie")

def score():
    print("\nYour score  -",You)
    print("Com score -",Com,"\n")


def play_game():
    player_1()
    player_2()
    winner()
    Tie()
    score()

while True:
    play_game()


    
