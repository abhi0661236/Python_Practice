import time

# getting the seconds from the epoch
seconds = time.time()

print("The seconds from the epoch are :", seconds)

# gettint the local time

local_time = time.ctime(seconds)

print("The local time is : ", local_time)


# the sleep() function delays the execution of the program

time.sleep(5)
print("This line is printed after five seconds from current execution thread")

# printing local time with the localtime() function
current_time = time.localtime(seconds)
print(current_time)

# Using the gmtime() method to display time in struct time fuction

gmtimeresult = time.gmtime(seconds)
print(gmtimeresult)