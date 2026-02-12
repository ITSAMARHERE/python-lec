# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2)) # union of two sets
# s1.update(s2) # update s1 with s2
# print(s1,s2)

cities = {"Delhi", "Mumbai", "Bangalore", "Chennai"}
cities2 = {"Kolkata", "Chennai", "Hyderabad"}
cities3 = cities.symmetric_difference(cities2) # symmetric difference of two sets
cities4 = cities.difference(cities2) # difference of two sets
print(cities.isdisjoint(cities2)) # check if two sets are disjoint
print(cities3)
print(cities4)
item = cities.pop() # remove a random item from the set
print(item)