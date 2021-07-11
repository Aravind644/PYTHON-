# Python2
OPERATORS


1.write a function for arithmetic operators(+,-,*,/).
ex: a=10
    b=5
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    

2.write a method for increment and decrement operators(++,--)

* Python does not have unary increment/decrement operator(++,--).Instead to increment a value we use a+=1 or a=a+1
* simillary for decrement we use a-=1 or a=a-1
ex: a=10
    a+=1
    print(a)
    a-=1
    print(a)
    
    
    
3.Program to equal operator and not equal operators

* equal and not equal operators are(==,!=)
ex: a=10
    b=15
    if a==b:
      print('equal')
    else:
      print('not equal')
      
      
      
4.Write a program to find the two numbers equal or not.

ex: a=10
    b=15
    if a==b:
      print('equal')
    else:
      print('not equal')
      
      
      
      
5.programs on Logical AND ,OR operator and Logical NOT.

* Logical AND operator:
Logical operator returns True if both the operands are True else it returns False.
EX:a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")
    
 Logical or operator:
Logical or operator returns True if either of the operands is True.

EX:a = 10
b = -10
c = 0
  
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
  
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
    
    
 Logical not operator:
Logical not operator work with the single boolean value. If the boolean value is True it returns False and vice-versa.

EX:a = 10
  
if not a:
    print("Boolean value of a is True")
  
if not (a%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
    
    
    
    
    
6.Program for relational operators(<,<==,>,>==)

*  Greater than: This operator returns True if the left operand is greater than the right operand.

Syntax:
x > y
Example:
a = 9
b = 5
print(a > b)


Less than: This operator returns True if the left operand is less than the right operand.

Syntax:
x < y
Example:
a = 9
b = 5
print(a < b)


Greater than or equal to: This operator returns True if the left operand is greater than or equal to the right operand.

Syntax:
x >= y
Example:
a = 9
b = 5
print(a >= b)


Less than or equal to: This operator returns True if the left operand is less than or equal to the right operand.

Syntax: 
x <= y
Example:
a = 9
b = 5
print(a <= b)



7.Print the smaller and larger number


number=[54,67,43,89,21,34]
#sorting the list
number.sort()
#print the last element in the list for largest
print("largest elements is: ",number[5])
#print the first element in the list for smallest
print("Smallest elements is: ",number[0])
