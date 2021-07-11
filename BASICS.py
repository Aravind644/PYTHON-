# PYTHON
#BASICS


1.How to create a class,object,method and its signature

'''* Class are like blueprint or a prototype that we can define to use to creat objects.We create Classes by using the Class keyword.
* Class is a blueprint created by a programmer for an object.This defines a set of attributes that will characterize any object.
* Object is an instance of a class.This is  the realized version of the class.
* The functions are indented under the Class are called methods.Methods are a special kind of functions that are defined under the class.'''


2.Write a program to print your name.

method 1:
  Name="Aravind"
  print(Name)
  
Method 2:
        #Take input from user 
        Name=('enter your name:')
        print(Name)
        
  
3.Write a program for a Singel line comment,multi-line and documentation comment.

* In Python we use the hash symbol (#) to write a single line comment.
  ex: # This is my first progarm in python
      print('Hello world!')
      
* In Python we use thriple single or double quotes(' or ") to write multi-line comment.
  ex:
     ''' This is my first program
     in python and it was successfully 
     complied'''
     print('welcome to python')
 


4.Define variables for different Data Types int,Boolean,char,float,double and print.

 In Python Data Types are built-in functions.We dont assign a variable like int,float,Boolean etc.,
 ex:
   a=10
   b=3.14
   c=True
   d='Aravind'
   print(type(a))
   print(type(b))
   print(type(c))
   print(type(d))
   
  
  
  
5.Define the local and Global variables with same name and print both variables and   understand the scope of the variables.

* Global variables: The variables which are outside the function is called Global variables.
* Local variables : The variables which are inside the function is called Local variables.
ex: a=89
    def fun():
      a=56
      print(a)
      return
    print(a)
    fun()
    
    

6.Write a function to print your name and call the function from main method.

class Name:
  def fun():
    print('Aravind')
    return
  def main():
    Name.fun()
    return
Name.main()
    
