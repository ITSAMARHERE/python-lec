def calculateGmean(a,b):
    mean = (a * b)/(a+b)
    print(mean)

def isGreater(a,b):
    if a > b:
        print("First number is greater than second number")
    elif a < b:
        print("Second number is greater than first number")
    else:
        print("first and second numbers are equal")
a = 9
b  = 8
isGreater(a,b)
calculateGmean(a,b)

c = 5
d = 10
isGreater(c,d)
calculateGmean(c,d)
