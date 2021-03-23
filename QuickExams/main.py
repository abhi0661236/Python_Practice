# the symbol # starts a comment and comments does not execute
"""This 
is 
 a multiline comment"""

str1 = "this is me"
num = 12
num2 = 23.3
print("3 + 5 is equals to :", 3+5)
print("3 x 5 is equals to :", 3*5)
print("3 / 5 is equals to :", 3/5)
print("5 % 3 is equals to :", 5%3) # modulous operator
print("5-3 is equals to :", 5-3)
print("3 // 5 is equals to :", 3//5) # floor division

print("this is double quote \"")

mulstring = """This is a multiline string
this makes it easy to write a bigger ''"text"'' and even sentences"""
print(mulstring)





# lists
colleges = ['IIT', 'NIT', 'College of Engineering']

colleges[2] = 'IIIT'
print(colleges[2])
colleges.append("AEIIT") # adds the item at the end of the list
print(colleges)
colleges.insert(3, "AEIIT")
print(colleges)
colleges.remove("AEIIT")
print(colleges)
print(len(colleges)) # total items
print(max(colleges)) # Alphabetically higher
print(min(colleges)) # Alphabetically lower

# tuples

tup1 = (1,3,4)
list1 = list(tup1)
print(tup1)
print(list1)


# dictionary
names = {'abhishek':18,
          'shashikant':19,
          'Ramdev':28}
print(names['Ramdev'])
print(names.keys())
print(names.items())
print(names.values())

# if-else statement
number = int(input("Enter a your age"))
print(number)

if number > 18:
    grade = 'A'
elif number > 10:
    grade = 'B'
elif number > 8:
    grade = 'C'
else:
    grade = 'D'

print('grade is :', grade)



# loops in Python

for i in range(0, 10):
    print(i)


list1 = ['item1','item2', 'item3']
for item in list1:
    print(item)

list1 = [[1,2,3],[4,5,6], [7,9,0]]
for item in list1:
    for i in item:
        print(i)
    


# While loops
print("Enter a number: ")
number = int(input())

while(number>4):
    print('Number is greater than 4.')
    number = int(input())
    if number == 9:
        break
    if number == 8:
        continue
    print("loop Ended")

import s