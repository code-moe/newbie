#name   : Python Conditional Statement
#author : CodeMoe
#date   : August 19,2019

#combine function with conditional statement if ... else
#Simple function : If your age is less than 25 YO, You are qualified
def age(): #head
  #body of function
  import datetime
  yBirth = input("Your birth year : ")
  yNow = datetime.datetime.now()
  Age = int(yNow.year) - int(yBirth)
  #Conditional Statement example:
  if Age > 25 :
    print("Your age now is",Age,"years old\nCurrently your age is older than 25 YO")
  else :
    print("Your age now is",Age,"years old\nYou are what we needed")
  #function body end

age() #Here run the function

#Simple program give different statement from 3 possible result
def rolldice(): #head
    from random import randint
    roll = randint(0,2) #possible result from roll = {0,1,2}
    #if ... elif ... else structure 
    if roll == 1:
        print("PHYTON FTW!!! Number:",roll)
    elif roll == 2:
        print("You are DEATH!! Number:", roll)
    else:
        print("Meh, you got",roll,"!! Z E R O")
        
        
