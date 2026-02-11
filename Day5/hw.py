#Create a python program capable of greeting you with
#Good Morning, Good Afternoon, or Good Evening 
#depending on the time of day.Your program should use time module to get the current hour.

import time;
t = time.strftime("%H:%M:%S")
hour = int(time.strftime('%H'))
hour = int(input("Enter the current hour (0-23): "))
print(hour)

if (hour>=0 and hour<12):
    print("Good Morning Sir!")
elif (hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif (hour>=17 and hour<21):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")