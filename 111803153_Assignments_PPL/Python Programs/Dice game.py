from random import *
import time
import sys

while True:
    n = randint(1, 6)
    print("1. Guess the number")
    print("2. Quit")
    print()
    i = int(input("Choose any one of the above"))
    if i == 1:
        num = int(input("Enter the number you guessed : "))
        if num == n:
            print("Congratulations You guessed the number")
        else:
            print("You guessed it wrong")
    if i == 2:
        break
    
        
        
    
    