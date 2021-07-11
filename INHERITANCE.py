# python7
INHERITANCE


1.A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members


sol:

class A:
    def fun(self):
        print('grand')
        return
    def fun11(self):
        print('Grand')
        return
    def fun12(self):
        print('GRAND')
        return
class B(A):
    def fun(self):
        print('grand')
        return
    def fun21(self):
        print('son')
        return
    def fun22(self):
        print('SON')
        return
class C(B):
    def fun(self):
        print('grand')
        return
    def fun31(self):
        print('grandson')
        return
    def fun32(self):
        print('GRANDSON')
        return
class overridden:
    def main():
        obj=C()
        obj.fun()
        super(C,obj).fun()
        super(B,obj).fun()
        obj.fun31()
        obj.fun32()
        obj1=B()
        obj1.fun21()
        obj1.fun22()
        obj2=A()
        obj2.fun11()
        obj2.fun12()
        
        return
overridden.main()
