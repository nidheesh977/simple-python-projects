#Rupee vs Dollar
print("All country money value and currency name")
print("Country : ")



def KWD():
    print("Kuwaiti Dinnar")
    print("Options : ")
    print("  1 -  to Rupee\n  2 - Rupee to Dollar\n")
    currency=input("Select your option : ")
    while currency not in ["1","2"]:
        print("Select 1 or 2")
        currency=input("Select your option : ")

    currency=int(currency)

    if currency==1:
        amount=int(input("Dollar : "))
        amount=amount*75
        print(amount," Rs /-\n")

    elif currency==2:
        amount=int(input("Rupee : "))
        amount=amount/75
        print("$",amount,"\n")



def USD():
    print("Options : ")
    print("  1 - Dollar to Rupee\n  2 - Rupee to Dollar\n")
    currency=input("Select your option : ")
    while currency not in ["1","2"]:
        print("Select 1 or 2")
        currency=input("Select your option : ")

    currency=int(currency)

    if currency==1:
        amount=int(input("Dollar : "))
        amount=amount*75
        print(amount," Rs /-\n")

    elif currency==2:
        amount=int(input("Rupee : "))
        amount=amount/75
        print("$",amount,"\n")




        
        
