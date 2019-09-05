#name   : Python Lists Operation
#author : CodeMoe
#date   : August 13,2019

#Learn List Operation
#Life is like a Python list. You spend most of it in boxes. Sometimes the box is empty and sometimes the box is filled with different objects. And sometimes it’s a box within a box. I like to think of Python lists as boxes because the brackets look like a container. 

chocho = ['Cherry Fondue', 'Crunchy Frog',
          'Ram\'s Bladder Cup','Cockroach Cluster',
          'Anthrax Ripple','Spring Surprise']
print('here is list of chocho :')
print(chocho,'\n')
print('chocho[2] = ',chocho[2],'\n')

from random import randint #this import function randint
random_number = randint(0,len(chocho)-1)

print("Here are print random index :", chocho[random_number])

#list are heterogeneous, can put many types of variables. List are also mutable, you can change it, list can also be saved inside other lists..
print("for example : a = [1,2,3]")
print("              b = ['one','two',c]")
print("              c = [3,'4','five']")
a=[1,2,3]
c = [3,'4','five']
b=['one','two',c]
d=[a,b]
print('reslt t[a,b]:',d,'\n')
d+='aaa'
#Concate (Join) and Multiply List
print('You can concate and multipy list')
print('t+="aaa"    : ',d)
d+=['aaa']
print('t+=["aaa"]  : ',d)
print('d*2         :',d*2)
print()
#Slicing and Delete List
print('Slicing and Delete lists :')
print('t[:-4] = : ',d[1:-4])
print('t        : ',d)
del d[0]
print('del t[0] : ',d)
del d[1:]
print('del t[1:]: ',d)
#Interesting func I find accidentally on discord
##print(list( set(a) & set(c))
