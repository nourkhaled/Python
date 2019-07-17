# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:43:18 2019

@author: IST List Less Than Ten
"""

 def less_than_Ten(lst):
 newlst = []
    for j in lst :
        if j < 10: 
            newLst.append(j)
            
         
    return (newLst)
            
            
lst = []
n = int (input ("Enter number of a list elements you want: ")) 

for i in range (0,n) :
    element = int (input())
    lst.append(element) 
    
    print (less_than_Ten(lst))
        
        