# ------------------------------
# Python Lists and Dictionaries
# ------------------------------

# Exercise 1

zoo_animals = ["pangolin", "cassowary", "sloth", "panda" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

# Exercise 2

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers [3]

# Exercise 3

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "panda"

# Exercise 4

suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shirts")
suitcase.append("shoes")
suitcase.append("pants")



list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# Exercise 5
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]               # Third and fourth items (index two and three)
last   = suitcase[4:6]                # The last two items (index four and five)

# Exercise 6
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end

#Exericse 7
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")


print animals # Observe what prints after the insert operation

# Exericse 8
my_list = [1,9,3,8,5,7]

for number in my_list: # "for" runs for how many items there are in a list
    # Your code here
    print 2 * number

# Exercise 9

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for numbers in start_list:
    square_list.append(numbers**2)

print square_list.sort()

# Exercise 10

# Dictionaries are like lists, but they store stuff with a key
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
#				key		value

# Used for name/password, name/phone number, etc.

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']

# Exercise 11
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Pasta'] = 7.00
menu['Mozarella sticks'] = 4.00
menu['Garlic bread'] = 2.00


print "There are " + str(len(menu)) + " items on the menu."
print menu

# Exercise 12
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Panda'

print zoo_animals

# ------------------------------
		"""SuperMarket"""
# ------------------------------

#Exercise 1
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for n in names:
    print n

# Exercise 2
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for k in webster:
    print webster[k]

# Exercise 3
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for numbers in a:
    if numbers%2==0:
        print numbers

# Exercise 4

# Write your function below!
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count+1
    return count

# Exercise 5
for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

# Exercise 6
prices = {
    "banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}

# Exercise 7
prices = {
    "banana": 4, # Don't forget commas after values in the key
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

# Exercise 8
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key] # Make sure to use %s here.
    print "stock: %s" % stock[key]

# Exercise 9
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

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0
for key in prices:
    print prices[key] * stock[key]
    total = total + prices[key] * stock[key]

print total

# Exercise 10
groceries = ['banana', 'orange', 'apple']

# Exercise 11
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

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        total = total + prices[item] # Kind of understand this one...
    return total

#Exercise 12
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

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item]>0: # Adding a conditional inside a loop inside a function inside a...
            total = total + prices[item]
            stock[item]=stock[item]-1
    return total
