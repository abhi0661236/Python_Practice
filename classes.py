"""
    Class: A class is an user-defined datatype.
    A class can have both the variables and the functions.
    And you can access them by creating an object of the class.
"""


'''
to create a class you have to use the keyword followed by the name of class

'''

class Alok:
    name ="alok shakya"
    """Now lets create a method"""
    def greet(name2):
        print("hello mr. :", name2)


    def __init__(self, name, age):
        """This function is by default"""
        self.name = name
        self.age = age


# Now lets create an object to access the elementes of the class alok

a = Alok

print(a.name_alok)


