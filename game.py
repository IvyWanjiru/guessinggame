#this program demonstrates a guessing
#game
from random import randint
#get the user input

player = input("enter value required")
print("hello player" + player +  "!")

#using a while loop
number=randint(10,50)

counter = 0
while counter<5:
    user_number=input(eval("enter user_number: "))


#get user number
#generate random number

#check is user input is equal to generated number
