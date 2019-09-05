#name   : Python Game Rock Paper Scissors
#author : CodeMoe
#date   : August 21,2019

#Iteration using for
#For 'every character' in 'string'
for char in 'for loop':
    print(char)
#Same with above just you can do more (Upper function)
for c in 'byting python':
    print(c.upper())
#Print number from a range
for number in range(10,20):
    print(number)

## If a chessboard were to have wheat placed upon each square
## such that one grain were placed on the first square, two on the second,
## four on the third, and so on (doubling the number of grains on each
## subsequent square), how many grains of wheat would be on the chessboard
## at the finish?
rice = 1
total = 0
# 2* range
for i in range(1,65):
    total += rice
    print("The amount of rice on square", i, "is: ", rice)
    print("Out total amount of rice is:", total)
    rice = rice * 2
