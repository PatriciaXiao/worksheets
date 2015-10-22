#!/usr/bin/env python
# coding: utf-8
"""
This examples should help with understanding dictionaries.
Fix all the lines with the FIX ME
"""

################################################################################
# Exercise 0 : Create a dictionary with an example that makes sense
# Phonebook, movies to stars, anything!
################################################################################
my_dict_1 = {'loi': 2, 'pitches': 4, 'intros': 4} # FIX ME
print("\nExercise 0")
print("I just invented the dictionary ", my_dict_1)

################################################################################
# Exercise 1 : Count the elements in a dict
################################################################################
print("\nExercise 1")
print("my_dict_1 has {0} pairs".format(len(my_dict_1))) # FIX ME

################################################################################
# Exercise 4 : Print all the keys
################################################################################
print("\nExercise 4")
print("The keys in the dict are ", my_dict_1.keys()) # FIX ME
#for key in my_dict_1:
	#print key

AND:  
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster: 
    print webster[key]


################################################################################
# Exercise 5 : Print all the values
################################################################################

print("\nExercise 5")
print("The values in the dict are ", my_dict.values()) # FIX ME
#for key in my_dict_1:
     #print my_dict_1[key]

################################################################################
# Exercise 6 : Print sequentially, all pairs (key, value)
################################################################################
print("\nExercise 6")
#for key, value in my_dict_1.items(): #try iteritems if item does not work  
    #print key, value[key]


#print "The keys and values in my_dict_1 are: %s" %my_dict_1
print "The keys and values in my_dict_1 are", my_dict_1

or 
print my_dict_1.items()

################################################################################
# Exercise 7 : Print sequentially, all pairs (key, value) and an index using 
# the enumerate
################################################################################
print("\nExercise 7 - using enumerate")
# Option 2 : Enumerate

#for key, value in enumerate(my_dict_1): # FIX ME
    #print key, value

for index, key in enumerate(my_dict_1.keys()): #getting a list with all the keys
    print index, key, my_dict_1[key] 


sorted_keys = sorted(my_dict_1.keys())
for key in sorted_keys:
	print key, my_dict_1[key]

################################################################################
# Exercise 8 : Invert the dictionary, that, is, make a new dictionary where
# the new keys are the old values and the new values are the old keys. 
################################################################################
#haven't tested this yet 
my_inverted_dict = dict([(v,k) for k, v in my_dict_1.iteritems()]) # FIX ME
#dict is a method 
print("\nExercise 8 - invert a dict")
print("Inverting keys in values in my_dict_1 gives", my_inverted_dict)

OR: 
for key in my_dict_1:
	invert_dict[ my_dict_1[key] ] = key


################################################################################
# Exercise 9 : Print the dictionary alphabetically by key
################################################################################
print("\nExercise 9: the dict in ascending order by key")
for key in {}: # FIX ME
    print key

################################################################################
# Exercise 10 : Print only the cities in california
################################################################################
cities = {"San Francisco":"CA", "New York":"NY", "Oakland":"CA", 
          "Los Angeles":"CA", "Seattle":"WA", "Detroit":"MI", "Jacksonville":"FL"}
print("\nExercise 10")
#for key in {}: # FIX ME
    #print("I love {0} because it's a city in California".format(key)) # FIX ME

if cities.has_key("California"):
	print cities

################################################################################
#print the key, followed by a space, followed by the value associated with that key.
################################################################################

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key, d[key] 
################################################################################
#Other examples
################################################################################

my_dict = {"Day 1": "Monday", "Day 2": "Tuesday", "Day 3": "Wednesday"}

#print my_dict.keys()
#print my_dict.values()

for key in my_dict: 
    print key, my_dict[key]

################################################################################


prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

    
total = 0
for key in prices:
    n = prices[key] * stock[key]
    total = total + n
    
print total 
################################################################################
    
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(food): 
    total = 0
    for item in food: 
        total += prices[item] ************!!!!!!
    return total 
    
def compute_bill(food): 
    total = 0
    for item in food: 
        if stock[item] > 0: 
            total += prices[item] ************!!!!!!
            stock[item] -= 1 
    return total 
        