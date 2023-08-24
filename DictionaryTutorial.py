capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

"""
Above, capitals is a dictionary object which contains key-value pairs inside { }. 
The left side of : is a key, and the right side is a value. 
The key should be unique and an immutable object. A number, string or tuple 
can be used as key. Here are some more examples.
"""
example_d = {} # empty dictionary

example_numNames={1:"One", 2: "Two", 3:"Three"} # int key, string value

example_decNames={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"} # float key, string value

example_items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} # tuple key, string value

example_romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} # string key, int value

"""
BAD IDEA!
A dictionary with a list as a key is not valid, as the list is mutable:
dict_obj = {["Mango","Banana"]:"Fruit", ["Blue", "Red"]:"Color"}

"""

"""But, a list can be used as a value."""
dict_obj = {"Fruit":["Mango","Banana"], "Color":["Blue", "Red"]}

"""
The same key cannot appear more than once in a collection. 
If the key appears more than once, only the last will be retained. 
The value can be of any data type. One value can be assigned to more than one key.
"""

numNames = {1:"One1", 2:"Two", 3:"Three", 2:"Two", 1:"One2"}

#Guess which values will appear? Remove hashes to experience the magic!
#print(numNames)

#The dict is the class of all dictionaries, as shown below.
#print(type(numNames))

"""
Dictionary is an unordered collection, 
so a value cannot be accessed using an index; 
instead, a key must be specified in the 
square brackets, as shown below.

We will use the capitals dictionary at the top of the file for this.
capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
"""

# Try each of the searches below
# print(capitals["USA"])
# print(capitals["France"])

# print(capitals["usa"])
# print(capitals["Japan"])

"""
Note keys are case sensitive and with this method 
it will generate an error if it can't find the key.

Use the get() method to retrieve the key's value even if keys are not known. 
It returns None if the key does not exist instead of raising an error.
"""

# print(capitals.get("USA"))
# print(capitals.get("France"))
# print(capitals.get("usa"))
# print(capitals.get("Japan"))


"""
Access Dictionary using For Loop
Use the for loop to iterate a dictionary in the Python script.
"""

#for key in capitals:
#    print("Key = " + key + ", Value = " + capitals[key]) 

"""
Update Dictionary
As mentioned earlier, the key cannot appear more than once. 
Use the same key and assign a new value to it to update the dictionary object.
"""
captains = {"England":"Root", "Australia":"Smith", "India":"Dhoni",'Srilanka': 'Jayasurya'}
#captains['India'] = 'Virat'
#captains['Australia'] = 'Paine'
#print(captains)

"""
Deleting Values from a Dictionary
Use the del keyword, pop(), or popitem() methods to delete a pair from a dictionary 
or the dictionary object itself. To delete a pair, use its key as a parameter. 
To delete a dictionary object, use its name.
"""

# del captains['Srilanka'] # deletes a key-value pair
# print(captains)
# del captains # delete dict object
# print(captains)

"""
The dict.popitem() method removes and returns a tuple of (key, value) 
pair from the dictionary. Pairs are returned in Last In First Out (LIFO) order.
The following example demonstrates the dict.popitem() method.
"""

romanNums = {'I':1, 'II':2, 'III':3 }
# print(romanNums.popitem())
# print(romanNums.popitem())
# print(romanNums.popitem())
# print(romanNums)
# print(romanNums.popitem()) # Is that one too many? Will generate error


# You might want to check the dictionary isn't empty before popping
#iamempty = {}
#print(len(iamempty))
#if not iamempty: print("I am empty")

"""
Retrieve Dictionary Keys and Values
The keys() and values() methods return a view 
objects containing keys and values respectively.
"""

d1 = {'name': 'Steve', 'age': 21, 'marks': 60, 'course': 'Computer Engg'}
#print(d1.keys())
#print(d1.values())

"""
You can check whether a paritular key exists in a dictionary collection or 
not usng the in or not in keywords, as shown below. 
Note that it only checks for keys not values.
"""

# print('England' in captains)
# print('India' in captains)
# print('France' in captains)
# print('USA' not in captains)

"""
Multi-dimensional Dictionary
Yes you can have dictionaries within dictionaries
"""

students = {101: {'name': 'Steve', 'age': 25, 'marks': 60},
            102: {'name': 'Anil', 'age': 23, 'marks': 75},
            103: {'name': 'Asha', 'age': 20, 'marks': 70}}

#print(students[101])
#print(students[101]['age'])


"""
This has been adapted from: https://www.tutorialsteacher.com/python/python-dictionary 
"""
