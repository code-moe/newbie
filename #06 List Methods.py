#name   : Python Lists Methods
#author : CodeMoe
#date   : August 14,2019

#Learn List Methods
#Remember to write all the func in lower case
print("You can do this on lists:")
print("1.Append()")
print("2.Extend()") 
print("3.Remove()")
print("4.Pop()")
todo = ['Go to the store', 'Play', 'Sing a tune or song', 'Eat', 'Draw', 'Drink', 'Get dizzy', 'Sit down']
print("todo : ",todo)
print()
#append = append to end of list
todo.append('Save the world')
print("#todo.append('Save the world'):\ntodo : ",todo)
print()
#extend = append the container list from another list
todo_yesterday = ['Sleep','Died']
todo.extend(todo_yesterday)
print("yesterday : ",todo_yesterday)
print("#todo.extend(yesterday):\ntodo : ",todo)
print()
#remove = remove a value in a list
todo.remove('Save the world')
print("#todo.Remove('Save the world')\ntodo : ",todo)
print()
#pop = not to be mistaken with poop, uups haha
#pop = remove and take a value from that list
todo_pop0 = todo.pop(0)
print("#todo_pop0 = todo.Pop(0)\ntodo : ",todo)
print("todo_pop0 = ",todo_pop0)