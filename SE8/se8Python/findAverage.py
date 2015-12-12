# We need to create a variable for each class...
math = float(input("What is your grade in Math?"))
ela = float(input("What is your grade in ELA?"))
softwareEngineering = float(input("What is your grade in Software Engineering?"))
science = float(input("What is your grade in Science?"))
socialStudies = float(input("What is your grade in Social Studies?"))

# now, we need to find the mean/average of our grades.
average = (math + ela + softwareEngineering + science + socialStudies)/5

print "Your average is a " + str(average) # what does str() do? Why do I need to use it?
