# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:46:21 2019

@author: IST
"""

def checkWinner (player1_wrd , player2_wrd):
    
    if player1_wrd == "paper" and  player2_wrd =="Rock":
        print("The Winner is  player 1 ... Congratulations! \n")
    elif player2_wrd == "paper" and  player1_wrd =="Rock":
        print("The Winner is  player 2 ... Congratulations! \n")
    elif  player2_wrd =="paper" and  player1_wrd == "Scissors":
        print("The Winner is  player 1 ... Congratulations! \n")    
    elif  player1_wrd =="paper" and  player2_wrd == "Scissors":
        print("The Winner is  player 2 ... Congratulations! \n")
    elif  player1_wrd =="Rock" and  player2_wrd =="Scissors":
        print("The Winner is  player 1 ... Congratulations! \n")
    elif  player2_wrd =="Rock" and  player1_wrd =="Scissors":
        print("The Winner is  player 2 ... Congratulations! \n")
        
        
wrd1 = input ("Enter Player1 Word :")
wrd2 = input ("Enter Player2 Word :")

checkWinner(wrd1,wrd2)