#model calculator

def Denomination():
    Two_thousand=int(input("    No of 2000 : "))
    Two_thousand=Two_thousand*2000
    Five_hundred=int(input("    No of 500  : "))
    Five_hundred=Five_hundred*500
    Two_hundred=int(input("    No of 200  : "))
    Two_hundred=Two_hundred*200
    Hundred=int(input("    No of 100  : "))
    Hundred=Hundred*100
    Fifty=int(input("    No of 50   : "))
    Fifty=Fifty*50
    Twenty=int(input("    No of 20   : "))
    Twenty=Twenty*20
    Ten=int(input("    No of 10   : "))
    Ten=Ten*10
    print("\nTwo thousand's =",Two_thousand//2000," =",Two_thousand)
    print("Five hundred's =",Five_hundred//500," =",Five_hundred)
    print("Two hundred's  =",Two_hundred//200," =",Two_hundred)
    print("Hundred's      =",Hundred//100," =",Hundred)
    print("Fifty's        =",Fifty//50," =",Fifty)
    print("Twenty's       =",Twenty//20," =",Twenty)
    print("Ten's          =",Ten//10," =",Ten)
    
    Total=Two_thousand+Five_hundred+Two_hundred+Hundred+Fifty+Twenty+Ten
    print("Total amount   =",Total)
Denomination()
while True:
    print("\nNew denomination : ")
    new=input("Press enter to continue and E to exit : ")
    if new=="E" or new=="e":
        break
    else:
        Denomination()
    






