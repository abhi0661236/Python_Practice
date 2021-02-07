# just practicing from scratch

a = "abhishek"                # A variable that holds a string
print(type(a))                # Just printing the type of the variable using type() method

# you can perform a type conversion or type casting of a variable using specific constructors
# such as

# a = int(a) # int() constructor will only convert the arguements if it is possible
# in this case it is impossible to convert a name into an integer so it will cause an error

b = 5; # for now b is a integer
print(type(b)) # this line prints <class 'integer'>
b = str(b)  # now it will be converted in string
print(type(b)) # and now it is printing <class 'str'>

# other constructors are float() int() complex()
# but remember you can not convert complex number into another number type



# It is time to dive deep into strings
# Just remember we have a string a = "abhishek" so it is a string literal

b = a[0] # don't forget we can reassign a variable so now variable b is holding the first charecter of
# the string a which is "a"
# a[0] = "c" #will give an error means that we can not update or change the string initially
# we can only access items using index number because strings are nothing but an object in python

del a # this will delete the string a completely
# and now you can not use the string a because it is no more avilble in the program

a = "abhishek"
b = 'prajapati' # notice we can define a string with both single and double quotes

mulStr = """ See we can have a multiline
string with these triple quotes"""
mulStr1 = '''Does not matter whether it is single or double 
quotes it is gonna work fine'''

# In result the line breaks will occur at the same positon where we have inserted in the string.

a = "hello dear"
b = a[2:4] # this is called slicing
# above variable will hold the string from index number 2 (included) to index number 4 (excluded)

# negative indexing is possible in python
b = a[-1] # here b is holding the last charecter of the string a
b = a[-10] # here b is overwritten by the first charecter of the string a. Do not forget to count the
# spaces of the string.
# you can slice strings in the same manner too.

# there are various string method you can perform on a string literals
# a few of them is mentiond below.


# strip() method removes any white spaces from the string literals from starting and ending of the string
a = "  hello abhishek"
print(a) # a have some whitespaces in starting
a = a.strip() # now a does not have any whitespaces in the starting.
print(a)
# lower() method returns a string in the lower case
a = a.lower()
print(a)
# upper() method returns a string in the upper case
a = a.upper()
print(a)
# count() method returns the occurances of a charecter in astring
b = a.count("L") # will return 2
print(b) # prints