#A dictionary is an unordered collection of items
#A dictionary has a key and a value pair

#empty dictionary
empty_dict = {}

#integer keys
integer_dict = {1: "name", 2: "location"}

#mixed keys
mixed_dict = {1: ["hello"], 'name': 2}

#To access elements from a dictionary the key can be used inside square brackets or with the get()
print(integer_dict.get(1))
print(mixed_dict['name'])

#To add or change things in a dict

#updating a value
integer_dict[1] = 20000

#adding a value
integer_dict[3] = "address"

#Now waht if we want to delete or remove elements from a dictionary

#To remove an items
print(mixed_dict.pop('name'))

#or you could do the follow
del mixed_dict[1]

#Dictionaries are heklpful for looking for membership, for example
print( 4 in integer_dict)
#this will output False
