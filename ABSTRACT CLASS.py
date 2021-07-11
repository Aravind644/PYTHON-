# python9
ABSTRACT CLASS


1.Create an abstract class with abstract and non-abstract methods

* Python comes with a module called abc which provides useful stuff for abstract class.
We can define a class as an abstract class by abc.ABC and define a method as an abstract method by abc.abstractmethod. ABC is the abbreviation of abstract base class.

from abc import ABC, abstractmethod

class Animal():
    @abstractmethod
    def move(self):
        pass
a = Animal()


2.Create a sub class for an abstract class.Create an object in the child class for the abstract class and access the non-abstract methods

* By subclassing directly from the base, we can avoid the need to register the class explicitly. In this case, the Python class management is used to recognize PluginImplementation as implementing the abstract PluginBase. 
 
 import abc
 
class parent:      
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        print("child class")
 
print( issubclass(child, parent))
print( isinstance(child(), parent))


3.Create an instance for the child class in child class and call abstract methods

import abc
 
class parent:      
    def geeks(self):
        pass
 
class child(parent):
    def geeks(self):
        print("child class")
print( issubclass(child, parent))
print( isinstance(child(), parent))


