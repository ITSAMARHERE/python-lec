letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Amar"

print(letter.format(name,country)) #format method
print(f"Hey my name is {name} and I am from {country}") #f-string method
print(f"{2*30}") #f-string method with expression
print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")  #to print curly braces in f-string we use double curly braces