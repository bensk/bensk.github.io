# If you want emoji in strings in Python 2.7, write
print u"🐙"

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

# Exercise 18

from math import sqrt # one way to import
print sqrt(13689)

import math # another way to import
print math.sqrt(9)

# Exericse 19 Review Built-in Functions
def is_numeric(num):
    return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2

def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"

# More Functions
"""This is my way. Codecademy does it different below"""
def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == "charlotte".lower():
        return 183
    elif city == "tampa".lower():
        return 220
    elif city == "pittsburgh".lower():
        return 222
    elif city == "los angeles".lower():
        return 475

print plane_ride_cost(raw_input("Which city?"))
"""Codecademy way"""
def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >=3:
        cost = cost -20
    return cost

# Exercise 7 Final trip_cost function
def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >=3:
        cost = cost -20
    return cost
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
