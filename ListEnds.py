# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:16:09 2019

@author: IST
"""

def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]


a = [1,2,3,4,5]
print (list_ends(a))
