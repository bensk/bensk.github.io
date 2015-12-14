score = 0

harry_potter = raw_input("What's Harry Potter's middle name?")
if harry_potter.lower() == "james":
    print u"⚡You're ok⚡" # To get emoji to print correctly, put a u for 'unicode' before a string.
    score = score + 1
else:
    print u"💥Expeliarmus!💥"

grace_hopper = raw_input("Grace Hopper coined what Computer Science term? A) Byte, B) Function, C) Iterate, D) Debug")
if grace_hopper.lower() == "d" or grace_hopper.lower()=="debug":
    print u"🐞You remembered!🐞"
    score = score + 1
else:
    print u"😭No! You make me sad...😭"

print "Your score is " + str(score) + " / 2"
