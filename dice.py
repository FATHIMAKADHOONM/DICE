#random
import random
import time

user_choice = "yes"
while user_choice=="yes" or user_choice=="y":
    print("Dice is rolling...")
    time.sleep(1)

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    print("Dice-1 : ",dice1,"\nDice-2 : ",dice2)
    time.sleep(1)
    if(dice2 == dice1):
        print("HURRAY!!....YOU GOT SAME VALUES:-)")
    else:
        print("LOST...TRY AGAIN!")

    user_choice = input("Do you want to roll again?(yes/no)").lower() #YES,Yes,yes,y,Y =>y

print("Thank you!!...")

