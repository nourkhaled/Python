# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:23:38 2019

@author: IST
"""



def fibonacci (eleNum):
   
  i= 1
  if eleNum == 0 :
      fib = []
  elif eleNum ==1 :
      fib =[1]
  elif eleNum ==2:
      fib = [1,1]
  elif eleNum > 2:
      fib = [1,1]
      
      while  i < eleNum - 1:
          fib.append(fib[i] +fib [i-1])
          
          i+=1
  return fib

ele = int (input("Enter a number to generate a fiboncci with it ...."))
print(fibonacci(ele))
          
      
      
          