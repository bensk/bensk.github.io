# Need to put month and date in as integers. Could add some code to convert, like "July" to 7.
m=int(input("What is the month?"));
d=int(input("What is the day?"));
y=int(input("What is the year?"));

def binDate(m,d,y):
   print(bin(m)[2:] + " / " + bin(d)[2:] + " / " +bin(y)[2:]); # Used string slicing to remove the '0b' from the beginning of the numbers
binDate(m,d,y);
