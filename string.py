# single quotes
str1 = 'This is first string'

# double quotes
str2 = "thid id a double quouted string"

# triple quotes
str3 = """This is a triple double quoted string which is 
actually a myltiline string. And if it is not assigned to a variable, Python iterpreters
it"""
str4 = '''This is another triple single quoted string
and it is also a multiline string'''

# strings in python are indexed objects

name = "Abhishek Prajapati"
print(name[4]) # prints s
print(name[8]) # prints the white space between Abhishek and Prajapati

# Length of the string

print(len(name)) # Prints 18

# upper() method

uprString = name.upper() # returns a new string so we always need to assign a variable
print(uprString)

# lower() method 

lowString = name.lower()
print(lowString)

# replace() method
replString = name.replace("A", "a")
print(replString)

# count() function
print(name.count("h")) # prints 2 because h is occuring two times in our name string.
