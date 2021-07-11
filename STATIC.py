# Python5
STATIC


1.Write a class with 2 static variables, 2 Instance variables, 2 static methods, 2 instance
methods and a main method.


class Shape:
    # class or static variable 
    cat = 'Geometrical'
    
    def __init__(self, type):
        # instance variable
        self.typ = type
     # method to show data
    def show(self):
        # accessing class variable
        print('Shape is of category: ', Shape.cat)
        # accessing instance variable
        print('And shape is: ', self.type)


tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()
class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info():
        return "This is a student class"
# Instance Method Example in Python 
class Student:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def avg(self):
        return (self.a + self.b) / 2

s1 = Student(10, 20)
print( s1.avg() )


2.Print instance variables in static methods

class Student:
    name = 'Student'
     def __init__(self, type):
        # instance variable
        self.typ = type
    
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info(self):
        # accessing instance variable
        print('And shape is: ', self.type)
        return "This is a student class"
tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()    



3.Print static variables in Instance methods


class example:
        staticVariable = 5

    print(Example.staticVariable) # prints 5

    # Access through an instance
    instance = Example()
    print(instance.staticVariable) # still 5


4.Call instance methods in static methods


class Student:
    name = 'Student'
     def __init__(self, type):
        # instance variable
        self.typ = type
    
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    @staticmethod
    def info(self):
        # accessing instance variable
        print('And shape is: ', self.type)
        return "This is a student class"
tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()


5.Call static methods in instance methods

class Student:
    name = 'Student'
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        
        
    def avg(self):
        return (self.a + self.b) / 2

s1 = Student(10, 20)
print( s1.avg() )



6.Print all the static, instance variables in main method

 class Test:
    x = 10
    def __init__(self):
        self.a =10

 t = Test()       
 print("Instance Variables:",t.__dict__)
 
 
 

