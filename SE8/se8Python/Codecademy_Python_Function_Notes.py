# Exercise 2
def spam():
    """This is silly"""
    print "Eggs!"

# Exercise 4
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

# Exercise 6
def cube(number):
    return number**3

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

# Exercise 8
"""Importing stuff
Ask Python to print sqrt(25) on line 3."""
import math
print math.sqrt(25)

# Exercise 11
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

# Exercise 17 (with some additions...)
def shut_down(s):
    if s == "yes":
        print "Shutting down"
    elif s == "no":
        print "Shutdown aborted"
    else:
        print "Sorry"
shut_down(raw_input("What should I do?"))
