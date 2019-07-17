# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:50:31 2019

@author: IST
"""
newLst = []
lst = []
def less_than_Ten(lst):
   
    for j in lst :
        if (j < 10): 
            newLst.append(j)
         
    return (newLst)


n = int (input ("Enter number of a list elements you want: ")) 
for i in range (0,n) :
    element = int (input())
    lst.append(element) 
    

print ("here is a list with numbers less than ten:")
print (less_than_Ten(lst))