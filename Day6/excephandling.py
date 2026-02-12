# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range (1,11):
#      print(f"{int(a)} X {i} = {int(a)*i}")
# except :
#     print("Please enter a valid number")

# print("Some important code that should be executed")
# print("This is the end of the program")


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Number you entered is not a valid integer.") 
else: 
    print(f"You entered {num}")