# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:06:36 2019

@author: IST
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
def find_diff_elements (a , b):
    
    if  len(a) > len(b):
        for i in b :
            if i in a and i not in c :
                c.append(i)
    elif len(a) < len (b):
         for j in a :
             if j in b and j not in c :
                 c.append(j)
    return (c)
                  
               
print (find_diff_elements (a , b))


    