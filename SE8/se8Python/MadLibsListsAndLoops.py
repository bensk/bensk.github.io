import random

def madLibs():
  names = raw_input("Give a bunch of names").split()
  adjectives = raw_input("Give a bunch of adjectives").split()
  
  for name in names:
    print name + " is " + random.choice(adjectives)

madLibs()
