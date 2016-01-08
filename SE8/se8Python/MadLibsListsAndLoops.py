import random

def madLibs():
  names = raw_input("Give a bunch of names").split()
  adjectives = raw_input("Give a bunch of").split()
  name_index = len(names) - 1
  for name in names:
    print names[name_index] + " is " + random.choice(adjectives)
    name_index = name_index - 1

madLibs()
