from datetime import *
today=date.today()
print(today)

def moms_birthday():
    birthday=date(2020,9,18)
    days_left_for_birthday=birthday-today
    
    if days_left_for_birthday.days == 1:
        print("Tomorrow is moms birthday")

    elif days_left_for_birthday.days > 1:
        print(days_left_for_birthday.days,"Days left for Moms Birthday")

    elif days_left_for_birthday.days==0:
        print("Today is Moms birthday")

    elif days_left_for_birthday.days<0:
        print("Moms birthday no more in this year")
        if -days_left_for_birthday.days>1:
            print("Finished before",-days_left_for_birthday.days,"days")
        else :
            print("It was yesterday")
    
def yours_birthday():
    a=int(input("Year : "))
    b=int(input("Month : "))
    c=int(input("Date : "))
    birthday=date(a,b,c)
          
    days_left_for_birthday=birthday-today


moms_birthday()
yours_birthday()
