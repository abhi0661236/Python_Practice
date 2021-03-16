"""A RegEx, or Regular Expression, is a sequence of charecters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern """

"""Python has a builtin package called re, which can be used to work with Regular Expressions."""
import re

txt = "Hi I am abhishek"
x = re.search("^Hi.*abhishek$", txt)

if x:
    print("We have a match\n", x)
else:
    print("No match")

"""
findall() - Returns a list containing all matches.
search() - Returns a Match object if there is a match anywhere
           in the string.
split() - Returns a list where the string has been split at
          each mach.
sub() -   Replaces one or many matches with a string
"""
# using the findall() function
txt1 = "I am a python coder and I am a anthusiast"
x = re.findall("th", txt1)
y = re.findall("main", txt1)
print(x)
print(y) # prints an empty list

# using the split() function
txt2 = "This is shashikant and he is a bad boy."
x = re.split("s", txt2)
print(x)

# using the sub() function
txt3 = "Today is my examination of Python"
x = re.sub("s", "9", txt3)
print(x)
