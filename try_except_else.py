# I am going to learn the exception handling in python

# sometimes you know that there can be a problem in some operations
# So we can catch that exception and produce another output

# I am trying to write in a file named testfile.txt

try:
    fh = open("tstfit", "r")
    fh.write("The file is written successfully !!")
except IOError:
    print("Error: can't find the file.")
else:
    print("The file is written successfully")
    fh.close()