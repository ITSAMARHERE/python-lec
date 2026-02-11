tup = (1, 5, 6, "Amar", True)
# tup[0] = 2 #tuples are immutable
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1]) #negative index

if "Amar" in tup:
    print("present in the tuple")
tup2 = tup[1:4] #slicing a tuple creates a new tuple
print(tup2)

