# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:52:10 2019

@author: IST
"""

import random



checker = True
while checker == True:
    
    innum = int (input("Guess A Number between 0 and 9 .... "))
    rand = random.randint(0 , 10)
    if innum == rand :
        print(rand)
        print("Congrats.. you exactly guessed it")
        state = input("If you want to try again enter Yes/Y /n If you want to Exit enter Exit")
        if state != "Exit":
             checker = True
             continue
             rand = random.randint(0 , 10)
        else:
             state = False
             break
    elif innum == rand-1 or innum == rand+1 :
        print(rand)
        print("Your are Close to the correct one....")
        state = input ("If you want to try again enter Yes/Y /n If you want to Exit enter Exit")
        if state != "Exit":
             checker = True
             continue
             rand = random.randint(0 , 10)
        else:
             state = False
             break
    else:
         print(rand)
         print("Sorry you are far away from the right number :( .... \n") 
        
         state = input("If you want to try again enter Yes/Y /n If you want to Exit enter Exit /n")
         
         if state != "Exit":
             checker = True
             continue
             rand = random.randint(0 , 10)
             
         else:
             checker = False
             break
 
     
     
     
     
