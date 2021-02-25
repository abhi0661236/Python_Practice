

# welcome back to the session
# today's topic is function
# a function is a block of code that is executed only when it is called
# function are very useful because it reduces code complexity and repitition

# A function is defined using the keyword def in python
# followed by the name of function followed by a pair of parentheses and a colon.

def my_func():
    print("Hello abhishek")
    print("How are you ?")

# It will not execute until we call it.
# so lets call the my_func()

my_func()

# A function can take any number of arguemnets just seperate them with a comma.
# And also make sure that function is parameterized.

def greet(name):
    print("Hello Mr. ", name)

greet("Abhi")

#greet("abhishek","abhi") # will cause an error so give the arguement same as the number of parameters.

'''
    But in case you do not know the number of arguements to be taken from a function.
    You can use arbitrary arguements in parameter name. Just add a asterisk before the parameter name.
'''
def greetAgain(*name):
    print("Hello Mr. : " + name[3])

greetAgain("abhishek", "rahul", "shashikant", "Ram Sevak") # will greet only Ram Sevak because he is on the index no. 3

# Now lets understand the word kwargs
# k+w+args
# key word arguements are shortened to kwargs.

"""
    We can pass the arguements in key = value syntax. In this method the order of
    arguements does not matters.
"""

def greet2(person1,person2,person3):
    print("Hello Mr. :" + person2)

greet2(person1="abhishek",
       person2="abhi",
       person3="Ram")

"""
    If you do not know the exact number of keyword arguements that will be passed into your function.
    You should use arbitrary keyword arguments for that use ** before the parameter name.

Note that : Arbitrary keyword arguments are often shortened as **kwargs in python documentations.
"""

def greet3(**name):
    print("Hello Mrs. " + name['lname'])

greet3(fname = "abhishek",
       lname="prajapati")

"""
    Now let's see what is defualt argument for a function.
    Many time you will wish to return a value from a function even if any argument is not given.
    You can do it by assigning a value to the parameter.
"""

def greet4(name = "Admin"):
    print("Hello Mr. : " + name)

greet4("abhishek") # will print Hello Mr. : abhishek
greet4() # will print Hello Mr. : Admin   because Admin is the default value for name parameter.

"""
    You will be amazed to know that you can pass any type of data inside a python function.
    Yes, doesn't matter whether the data is string, number, or a list or any other collection.
"""

def greet_all(user):
    for x in user:
        if x == "Shalu Mam" :
            print("Hello :" + x)
        else:
            print("Hello Mr. :" + x)

users = ["abhishek","Ram Sevak","Rahul","Lalit Sir","Shalu Mam"]
greet_all(users)

"""
    You can return a value or expression from a function after performing defined action
    If you try to return an expression from a fuction the return statement will solve the expression first and then
    return the value.
"""

def square(num):
    return num*num

print("The square of the given number is :", square(5))

"""
    You will get an error if you left a function definition blank. However in programming many situation
    will arise that needs a blank function definition. You can overcome the situation by simply using the pass statement.
"""
def new_func():
    pass

new_func() # This function call will do nothing. There is no definition inside this function


# Now comes the most interesting part of the function and I would say most dangerous part too. That is Recursion
"""
    When a function call itself inside it for some reason, this process is called recursion.
    Recursion is a dangerous too because if you by mistake create a function that's condition never evaluates to false
    the function will keep looping through itself and can consume a large amount of memory and processor's effort.
    But if it is written correctly, can be used in a very elegant manner in programming.
"""

def tri_recurse(k):
    if(k > 0):
        result = k + tri_recurse(k-1)
        print(result)
    else:
        result = 0

    return result

print("\n\nRecursion example result is :")

tri_recurse(3)