dic = {
    "name": "Amar",
    "age": 21,
}

print(dic["name"])  # Output: Amar

info = {'name': 'Karan', 'age': 22, 'eligible': True}
# print(info)
# print(info['name'])
# print(info.get('name'))
# print(info.keys())
# print(info.values())
# for key in info.keys(): print(f'The value corresponding to the key {key} is {info[key]}')

print(info.items()) # returns a list of tuples containing key-value pairs
for key, value in info.items():
 print(f'The value corresponding to the key {key} is {info[key]}')