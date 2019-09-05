#name   : Python Strings
#author : CodeMoe
#date   : August 10,2019

print("You can do four operations on string type variable")
print("1. First is Concatenation")
print("e.g -> ab = 'a' + 'b' ")
ab='a'+'b'
print('result of operation = '+ab)
print('')
print('2. Second is Multiplication')
print("e.g -> ab = ab*10 ")
print('result of operation = '+ab*10)
print('')
print('3. Third is Indexing')
print("e.g -> Croman = abc..xyz")
print("Croman[0] = index 0 of var Croma")
Croma='abcdefghijklmnopqrstuvwxyz'
print('result of operation : ')
print("Croman[0] = "+Croma[0])
print("Croman[1] = "+Croma[1])
print("Croman[25] = "+Croma[25])
print('')
print('4. Last is Slicing')
print("Croman[0:13] = character index 0 to 12")
print('Result of operation : ')
print("Croman[0:13] = "+Croma[0:13])

print("Croman[5:] = "+Croma[0:5])
print("Croman[0:5] = "+Croma[0:5])
#take char index 2 to 4
print("Croman[2:5] = "+Croma[2:5])
print("Croma[:5] = "+Croma[:5])
#indices backward with negative integer
print("Croma[-3:] = "+Croma[-3:])
print('')
#Methods on STRINGS
print("String Methods :") 
print("str(), upper(), lower(), count(), find(), replace() & len()")
print("Syntax example : ")
print("1. str(math.pi)")
print("2. Croman.upper()")
print("3. Croman.lower()")
print("4. Croman.count('a')")
print("5. Croman.find('a') or Croman.find('abcde') or Croman.find('a',5) or Croman.find('a',5,-10)")
print("RO>>> Find a ; Find abcde ; Find a start at index 4 ; Find a start at index 4 end at index -5")
print("6. Croman.replace('a','word','replaced_word')")
print("7. len(Croman)")
print("There were others, like Croma.capitalize()")