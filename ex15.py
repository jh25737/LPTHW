from sys import argv
#load the argv argument from sys
script, filename = argv
#script setting filename input command line
txt = open(filename)
#sets text to equal whatever user to whatever the opened inputed filename is
print "Here's your file %r:" % filename
#prints string with filename
print txt.read()
#print the contents of the filec
txt.close()

script, file_again = argv
#creates new variable equal to user input filename
print "Here's your file %s:" % file_again
txt_again = open(file_again)
#creates txt again and sets its value to the file
print txt_again.read()
#prints the files contexts
txt_again.close()