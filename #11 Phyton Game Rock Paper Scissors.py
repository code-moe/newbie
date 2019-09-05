#name   : Python Game Rock Paper Scissors
#author : CodeMoe
#date   : August 20,2019

#List of possible result
t = ["R","P","S"]
#import randint function
from random import randint

#You will restart the game until you win
condition = False
while condition == False :
    #Computer choice
    com = t[randint(0,2)]    
    #Your choice
    player = input("Your choice? ")
    print("Computer choice : ",com)         
    if player == com :
        print("Tie")
    elif player == 'R':
        if com == 'S':
            print("Win,",player,"smashes",com)
            condition = True #IF WIN BREAK
        else:
            print("Lose,",com,"covers",player)
    elif player == 'P':
        if com == 'R':
            print("Win,",player,"covers",com)
            condition = True #IF WIN BREAK
        else:
            print("Lose,",com,"cuts",player)
    elif player == 'S':
        if com == 'P':
            print("Win,",player,"cuts",com)
            condition = True #IF WIN BREAK
        else:
            print("Lose,",com,"smashes",player)
    else :
        print ("Wrong Input, Repeat...")

    





     
        
