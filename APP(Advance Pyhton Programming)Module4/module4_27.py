'''
In Python, inheritance is a mechanism that allows a class (subclass) to inherit methods and attributes from another class (superclass). 
This means that the subclass can reuse code from the superclass, promoting code reusability and maintaining a hierarchical structure.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Creating instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods inherited from superclass
print(dog.name + " says: " + dog.sound())
print(cat.name + " says: " + cat.sound())


'''
In this example, we have a superclass Animal with a constructor (__init__) that takes a parameter name. The sound method in the Animal class is a placeholder method that subclasses will override.

We then have two subclasses, Dog and Cat, which inherit from the Animal class. Each subclass defines its own implementation of the sound method.

The __init__ method, also known as the constructor, is a special method in Python classes. It is called automatically when an object is created. In the example, the __init__ method initializes the name attribute of an Animal object with the value passed during instantiation.

So, in summary, the __init__ method serves as a constructor in Python classes, initializing object attributes when an object is created. Inheritance allows subclasses to inherit methods and attributes from a superclass, promoting code reuse and maintaining a hierarchical structure.



'''