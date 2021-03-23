# List is one of the four basic data structure that provided by python by default
myList = ['abhishek', 'prajapati', 'Microsoft', 'Office']
print(myList)
myList[2] = 'Shashikant'
print("After changing the value Microsoft to Shashikant the list becomes")
print(myList)
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)
sliced = myList[1:3]
print(sliced)
slicedN = myList[-3:-1]
print(slicedN)
