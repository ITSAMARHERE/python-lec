# countries = ("Spain", "France", "Italy", "Germany", "Norway")
# temp = list (countries) #convert tuple to list
# temp.append("Sweden") #add element to the list
# temp.pop(3) #remove element at index 3
# countries = tuple(temp) #convert list back to tuple
# print(countries)
# print(temp)

tuple1=(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# res = tuple1.count(1) #count the number of occurrences of the element
# res = tuple1.index(1) #find the index of the first occurrence of the element
res = tuple1.index(1, 4,7) #find the index of the first occurrence of the element starting from index 1
print('Number of occurrences of 1:', res)