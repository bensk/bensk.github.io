grades = raw_input("What are your grades?").split() # Start out just like our old GPA calculator.
float_grades=[] # Make an empty list. We'll need this once we convert all of our grades to floats.

for inputs in grades: # This for loop will go through every grade...
  num_grade = float(inputs) # float() the value of each grade...
  float_grades.append(num_grade) # and append that float value to our empty list

# I've made a new variable. You don't NEED to do this, but it makes the last line look cleaner
average = sum(float_grades)/len(float_grades)

# Now that we're ready to print, we can just str() our average variable.
print "Your average is a " + str(average)
 
