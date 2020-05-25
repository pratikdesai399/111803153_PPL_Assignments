from random import *
from sys import *
rand_num = randint(1, 100)
cou = 0
while True:
    cou+=1
    if cou == 6:
        exit()
    
    
    print("Guess the number:")
    n = int(input())
    if n == rand_num:
        print("Bravo!!! You guessed the number")
        break
    if n < rand_num:
        print("Your guess is low. Try a number greater than this")
    if n > rand_num:
        print("Your guess is high. Try to guess it lower than this")

        
             

            
           
   
    

       
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
    