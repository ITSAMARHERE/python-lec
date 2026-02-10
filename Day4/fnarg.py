# def average(a,b):
#     print("The average is ", (a+b)/2)

# average(10,20)

# def average(*numbers):
#     sum = 0
#     for num in numbers:
#         sum += num
#     print("The average is ", sum/len(numbers))

#     average(10,20,30,40,50)

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(fname="John", mname="Fitzgerald", lname="Kennedy")