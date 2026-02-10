# l = [3,5,6]
# print(l)
# print(type(l))

marks = [3,5,6,"Amar",True]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-1]) #negative index
# print(marks[len(marks)-1]) #postive index
# print (marks[5-1]) #postive index
# print(marks[4]) #postive index

# if "Amar" in marks:
#     print("present in the list")
# else:
#     print(" not present in the list")

# print(marks)
# print(marks[1:-1]) #slicing
# print(marks[1:4])
# print(marks[1:4:2]) #jump index

lst = [i*i for i in range(4)] #list comprehension
print(lst)

lst = [i*i for i in range(10) if i%2==0] #list comprehension with condition
print(lst)