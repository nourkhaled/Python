# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:58:37 2019

@author: IST
"""

def check_PrimalityFn(num):
    if num == 2 :
        prime =True
    elif num == 1:
        prime = False
    else:
        prime = True 
        for checkNum in range (2 , (num - 1)):
            if num % checkNum != 0:
                continue
            elif num% checkNum == 0:
                prime =  False 
                break
    return prime    
    


num = int(input("Enter A number to check primality.....\n"))
prime = check_PrimalityFn(num)
print(prime)
if prime == False :
    print("It is not a Prime Number")
else:
    print("This is a prime number")
    

        