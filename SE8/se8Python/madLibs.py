def madLibs():
  name = raw_input("Give me a name").capitalize() # Why did I use .capitalize here?
  name1 = raw_input("Give me a name").capitalize()
  name2 = raw_input("Give me a name").capitalize()
  name3 = raw_input("Give me a name").capitalize()
  adj = raw_input("Give me an adjective")
  adj1 = raw_input("Give me an adjective") # Watch your variable names!
  adj2 = raw_input("Give me an adjective")
  adj3 =  raw_input("Give me an adjective")
  print name + " is " + adj
  print name1 + " is " + adj1
  print name2 + " is " + adj2
  print name3 + " is " + adj3

madLibs()
