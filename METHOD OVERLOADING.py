# python13
METHOD OVERLOADING




**  Method overloading is one concept of Polymorphism. It comes under the elements of OOPS. It is actually a compile-time polymorphism. It is worked in the same method names and different arguments. Here in Python also supports oops concepts. But it is not oops based language. It also supports this method overloading also.

Normally in python, we don’t have the same names for different methods. But overloading is a method or operator to do the different functionalities with the same name. i.e methods differ their parameters to pass to the methods whereas operators have differed their operand.

Here some advantages of Method Overloading in Python.

Normally methods are used to reduce complexity. Method overloading is even it reduce more complexity in the program also improves the clarity of code.
It is also used for reusability.
It has some disadvantages also when creating more confusion during the inheritance concepts.

In python, we create a single method with different arguments to process the Method Overloading. Here we create a method with zero or more parameters and also define the methods based on the number of parameters.


1.Write two methods with the same name but different number of parameters of same type
and call the methods from main method

class cal:
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return
    def add(a,b,c):
        res=a+b+c
        print('sum of 3 numbers:',res)
        return

class overload:
    def main():
        cal.add(10,20,30)
        cal.add(10,20) #error
        return
overload.main()



2.Write two methods with the same name but different number of parameters of different
data type and call the methods from main method

class cal:
    def add(a,b,c):
        res=a+b+c
        print('sum of 3 numbers:',res)
        return
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return

class overload:
    def main():
        cal.add(10,30)
        cal.add('aravind','reddy',10) 
        return
overload.main()





3.Write two methods with the same name and same number of parameters of same type
and call from main method

class cal:
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return

class overload:
    def main():
        cal.add(10,20)
        cal.add(10,30) 
        return
overload.main()



4.Write two methods with the same name and same number of parameters of different
type and call from main method


class cal:
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return
    def add(a,b):
        res=a+b
        print('sum of 2 numbers:',res)
        return

class overload:
    def main():
        cal.add(10,20)
        cal.add('aravind','reddy') 
        return
overload.main()



5.Write two methods with the same name, number of parameters and data type but
different return Type.


* It is not possible to have a method with same parameters and different return type. Compiler throws error in the below case(Duplicate method).


