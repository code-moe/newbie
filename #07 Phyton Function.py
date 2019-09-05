#name   : Python Function
#author : CodeMoe
#date   : August 14,2019

#Function printme 
def printme():
  print("The world is beautiful")
printme() #execute
print()
#Function snowclone with two 
def snowclone(x, y): #Function with two 
    print(x, "is the new", y, ".")
snowclone("Python", "Java")
print("-------------Limerick-------------")
def limerick(a,b,c,d,e):
  print("There once was an",a,"from place",b)
  print("Who satisfied predicate",c)
  print("The",a,"did Thing",d)
  print("In a specified way")
  print("Resulting in circumstance",e)
limerick("X","B","P","A","C")
print("---------------FLOW---------------")
def flow(left, right):
    print(right,left)
flow("(^_-)", "(-_^)")
print() #HERE IS FUNCTION TO CALC 2 VALUE
print("Calculate a + b")
a=int(input("Input a: "))
b=int(input("Input b: "))
def calculate(a,b):
  a+=b
  print(a)
calculate(a,b)
