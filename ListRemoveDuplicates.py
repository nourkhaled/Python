# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:43:34 2019

@author: IST
"""
 
def rmv_duplicates (lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst.append(i)
        else:
            continue
    return newlst    
a = [2,2,5,3,6,5,9]   
print (rmv_duplicates(a))