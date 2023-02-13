#program to guess the number using a while loop. 
import random
n = int(input("enter number"))
while(True):
    number = random.randint(1,20)
    if number == n:
        print("you guessed it right")
    else:
        print("oops better luck next time. the correct number was",number)
    break