"""
    Class: A class is an user-defined datatype.
    A class can have both the variables and the functions.
    And you can access them by creating an object of the class.
"""


'''
to create a class you have to use the keyword followed by the name of class

'''

class Alok:      # Classes are created by the keyword "class"
    name ="alok shakya" # variables inside a class is also known as attribute of the class. And can be accesssed by the . dot operator.

    def greet(self):  # self is the default parameter for the class methods. We do not give a value for this parameter when we call the method, Python provides it.
        """Method for greeting"""     # This is docstring which is used for function documentation.
        print("hello mr. :", self.name)


# Now lets create an object to access the elementes of the class alok
"""Objects are the instance of the class"""
a = Alok()   # object created

print(a.name)   # notice the use of . dot operator.












"""
    Now lets talk about classes that takes arguments :) yes it is possible.
    We can use constructor __init__() for this purpose.
    This constructor is used to take arguments at the time of object creatfion and immediately initialize
    the class attribute.
    To understand this better, let's create a new class named person
"""

class Person:
    # now let's create a constructor
    def __init__(self, name): # self is provided by python and name is what we will be passing at the time of object creation.
        self.person_name = name # passes value will be assigned in person_name variable.

    def namastey(self):
        print("Namastey", self.person_name)

# now let's create the object

myObject = Person("abhishek") # the string "Abhishek" will be assigned to the variable person_name

# let's call the function namastey
myObject.namastey()     # Notice that I didn't pass any argument for the function namastey()



