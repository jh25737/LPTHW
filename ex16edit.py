from sys import argv

script, filename = argv

print "We're going to eratse %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do wnt that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#removed trunctate command as 'w' mode already does this.

print "Now I'm going to ask you three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s" % (line1,line2, line3))


print "And finally, we close it."
target.close()