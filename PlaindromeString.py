# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:07:26 2019

@author: IST
"""

def reverse(wrd):
    x= '' 
    for i in range(len(wrd)):
        x += wrd [((len(wrd)-1)-i)]
        
    return x

    
wrd = input ("Enter a word:\n")
x = reverse(wrd)

if x == wrd :
   print ("The Word you have been entered is a Plaindrome word")
else :
   print ("The Word you have been entered is not a Plaindrome word")
        
        
       