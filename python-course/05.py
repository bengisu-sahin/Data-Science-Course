# Python program to illustrate
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2))) 

#OUTPUT 
"""
Return type: 
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

"""

"""
# Python3 program explaining work
# of randint() function

# import random module
import random

# Generates a random number between
# a given positive range
r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))

# Generates a random number between
# two given negative range
r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is % d" % (r2))

"""
"""
random.seed(5)
 
print(random.random())
print(random.random())

Output:

0.6229016948897019
0.7417869892607294
"""
