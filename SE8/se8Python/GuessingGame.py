user_name = raw_input("What's your name?").upper()
print "Hello there " + user_name

upper_bound = int(raw_input("What's the largest number you'd like to choose?"))

from random import randint

answer = randint(0, upper_bound)

guess = int(raw_input("What's your guess?"))

while guess != answer:
    # Got it to give me feedback!
    if guess>answer:
        print "Your guess is too high!"
    else:
        print "Your guess is too low!"
    guess = int(raw_input("What's your guess?"))

print "Great job, " + user_name + ", the number was " + str(answer)
# print randint(0,upper_bound) so, that works
