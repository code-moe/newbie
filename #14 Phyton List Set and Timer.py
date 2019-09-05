#name   : Python List Set and Timer
#author : CodeMoe
#date   : 23 August, 2019
#true-a : Code taken from Shirayuki-sama from Python Discord

#import modules Timer and ascii_letters
from timeit import Timer
from string import ascii_letters

#fill list_a & list_b with ascii letters
list_a = list(ascii_letters)
list_b = list(ascii_letters)

#return value 
def test1():
    """List comp"""
    return [i for i in list_a if i in list_b]
#return i for i in list a that's in list b (ALL)

#Set function to join same value that exists in both lists
def test2():
    """Set"""
    return list(set(list_a) & set(list_b))
#return set

#print function-return 
print(test1(), test2())

#you can use sorted() function to sort the list
#for example e.g. : sorted(test2())

for test in (test1, test2):
    print(f"{test.__doc__:<9} -> {Timer(test).timeit(10000):.2f}s")

