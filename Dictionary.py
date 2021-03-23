"""The dictionary is one of the basic data structure provided in python by default"""

# creation of dictionary
myDict = {
    'name':'Abhishek',
    'age':23,
    'branch':'IT',
    'address':'India',
    'college':'Govt. Polytechnic Ghaziabad'
}

# Accessing the data of the dictionary is possible with the help of keys we provided

a = myDict['name']
print("The name of this candidate is:", a, "And his age is :", myDict['age'])

# Let's create a nested dictionary

Branch = {
    'IT':{
        'Abhishek':{
            'fullname':'Abhishek Prajapati',
            'age':18,
            'add':'Azamgarh'
        },
        'Shashikant':{
            'fullname':'Shashikant Yadav',
            'age':19,
            'add':'Sonbhadra'
        },
        'Samrendra':{
            'fullname':'Samrendra Vishwakarma',
            'age':21,
            'add':'Prayagraj'
        }
    },
    'CIVIL':{
        'Alok':{
            'fullname':'Alok kumar',
            'age':19,
            'add':'Buland Shehar'
        }
    },
    'PRODUCTION':{
        'Nikhil':{
            'fullname':'Nikhil Gaitonde',
            'age': 22,
            'add': 'Ghazipur'
        }
    }
}

# let's access the data inside it

a = Branch.get('IT')
print(a)

b = Branch['CIVIL']
print(b)

print("the total branches are :", len(Branch))

c = len(Branch['IT'])
print("The total number of records in IT branch is: ", c)
print("The total number of records in CIVIL branch is: ", len(Branch['CIVIL']))

fullnameofAbhishek = Branch['IT']['Abhishek']['fullname']
print("The full name of Abhishek is: ",fullnameofAbhishek)

fullnameofAlok = Branch['CIVIL']['Alok']['fullname']
print("The full name of Alok is : ", fullnameofAlok)

# Just for testing 

testTravarsal = Branch.get('IT').get('Abhishek').get('fullname')
print(testTravarsal)

# O My God It worked just like the usual brackets notation
# Means that python follows the JSON
