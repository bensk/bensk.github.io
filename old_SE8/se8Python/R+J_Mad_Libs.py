print "The _______ of Romeo & _______"
print ".............................."

plural_noun = raw_input("plural noun".upper()).upper()
plural_noun1 = raw_input("Another plural noun".upper()).upper()
place = raw_input("place".upper()).upper()
noun = raw_input("noun".upper()).upper()
noun1 = raw_input("Another noun".upper()).upper()
adjective = raw_input("adjective".upper()).upper()
adjective1 = raw_input("One more adjective".upper()).upper()
verb = raw_input("verb".upper()).upper()
verb1 = raw_input("One more verb".upper()).upper()
number = raw_input("a number".upper()).upper()
body_part = raw_input("a body part".upper()).upper()

def madLibs():

    print "Two %s , both alike in dignity," % plural_noun
    print "In fair %s , where we lay our scene," % place
    print "From ancient %s break to new mutiny," % noun
    print "Where civil blood makes civil hands unclean."
    print "From forth the fatal loins of these two foes"
    print "A pair of star-cross`d %s take their life;" % plural_noun1
    print "Whole misadventured piteous overthrows"
    print "Do with their %s bury their parents` strife." % noun1
    print "The fearful passage of their %s love," % adjective
    print "And the continuance of their parents` rage,"
    print "Which, but their children`s end, nought could %s ," % verb
    print "Is now the %s hours` traffic of our stage;" % number
    print "The which if you with %s %s attend," %  (adjective1, body_part)
    print "What here shall %s , our toil shall strive to mend." % verb1

madLibs()
