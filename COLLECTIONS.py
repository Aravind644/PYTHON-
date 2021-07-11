# python16
COLLECTIONS


1.Create an ArrayList of type String with 10 string elements. Add 10 string elements to
ArrayList and perform the below operations
Add an element to the ArrayList
Iterate through the ArrayList by using Iterator object
Add an element at a specific index
Remove an element from the ArrayList, Remove at an index
Update the element at a specific index
Check the element is present at a particular index
Get an element at a particular index
Find out the size of the ArrayList
Check the given element is present in the ArrayList
Remove all elements of the ArrayList




*
import numpy as np
Arraylist=['apple','bat','cat','dog','egg','fan','gun','hat','ink','joker']
arr=np.array(Arraylist)
# add an element to the Arraylist

Arraylist.append('king')
print(Arraylist)

# iterator object

for x in Arraylist:
   print(x)
   
#get an element at a particular index
   
print(Arraylist[4])

#size of arraylist
print(len(Arraylist))

#Add an element at a specific index
Arraylist.insert(1,'bell')
print(Arraylist)

#Remove an element from the ArrayList
Arraylist.remove('bell')
print(Arraylist)

#Remove an element from the ArrayList at an index
Arraylist.pop(5)
print(Arraylist)

#Update the element at a specific index
Arraylist[2]='cry'
print(Arraylist)

#Check the element is present at a particular index
index =Arraylist.index('apple')
print('The index of apple is:', index)


platform = 'joker'
if platform in Arraylist:
  print('joker is in the Arraylist service business')
else:
  print('It does not include')

#Remove all elements of the ArrayList
Arraylist.clear()
print(Arraylist)
