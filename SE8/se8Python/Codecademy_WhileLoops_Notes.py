# Exercise 1

count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count

"""
The while loop is similar to an if statement: it executes the code inside of it if some condition is true. The difference is that the while loop will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.
"""

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

# Exercise 2

loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

# Exercise 3
num = 1

while num < 11:  # Fill in the condition
    print num ** 2
    num = num + 1
    # Print num squared
    # Increment num (make sure to do this!)

# Exercise 4
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

# Exercise 5
count = 0

while count < 10: # Add a colon
    print count
    # Increment count
    count = count + 1

# Exercise 6
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break # This is a way to stop the code from becomming an infinite loop

#Exercise 7
