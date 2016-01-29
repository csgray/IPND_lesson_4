"""Lesson 4.4: Modulus & Dictionaries
Modulus Operator %
<number> % <modulus> -> <remainder>

14 % 12 -> 2
"""

"""Lesson 4.4: Dictionaries

Dictionaries are another crucial data structure to learn in Python in
addition to lists. These data structures use string keywords to access
data rather than an index number in lists. Using string keywords gives
programmers more flexibility and ease of development to use a string
keyword to access an element in this data structure.

https://www.udacity.com/course/viewer#!/c-nd000/l-4181088694/m-3919578552
"""

# Strings vs List vs Dictionary Demo
s = "hello"
p = ["alpha", 23]
d = {"hydrogen": 1, "helium": 2}

# Accessing items
print s[2]
print p[1]
print d["hydrogen"]

# Replacing values
# s[2] = "a"  # Will produce error
p[1] = 999
d["hydrogen"] = 49

"""Different Types of data
String: sequence of characters, immutable, s[i]
List: list of elements, mutable, p[i]
Dictionary: set of <key, value> pairs, mutable, d["k"]
"""

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print elements
print "lithium" in elements

elements["lithium"] = 3
elements["nitrogen"] = 8

print elements["lithium"]
print elements["nitrogen"]

elements["nitrogen"] = 7
print elements["nitrogen"]

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0,
              "Mumbai": 12.5}

elements = {}
elements["H"] = {"name": "Hydrogen", "number": 1, "weight": 1.00794}
elements["He"] = {"name": "Helium", "number": 2, "weight": 4.002602,
                  "noble gas": True}
print elements["He"]["noble gas"]
