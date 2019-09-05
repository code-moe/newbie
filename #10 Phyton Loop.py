#name   : Python Loop
#author : CodeMoe
#date   : August 19,2019

#Here we are using while function to loop
#LOOP : Continue? 10 9 8 7 6 5 4 3 2 1 
count = 10
print("Continue? ",end="") 
while count > 0:
    print(count,end=" ")
    count-=1
print()
#LOOP : decrement
count = 10
while count > 0:
    print("\ncount before decrement: ", count)
    count-=1
    print("count after decrement:", count)
    print("count is still greater than zero, so… run the loop again!")
#LOOP : increment
count = 0
while count < 10:
    print("\ncount before increment: ", count)
    count+=1
    print("count after increment:", count)
    if count < 10 :
        print("count is still less than ten, so… run the loop again!")
#LOOP : infinite loop
#Press Ctrl + C to break
while True:
    print("impossible loop ctrl + c to exit")
    break
#LOOP : using break command to exit from loop
while True:
    ans = input("Are we there yet? ")
    ans = ans.lower()
    if ans.strip() == 'yes':
        break
    
