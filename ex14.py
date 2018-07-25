from sys import argv

script, first_name, last_name = argv
answer = '-'

print "Hi %s %s, I'm the %s script." % (first_name, last_name, script)
print "I'd like to ask you a few questions."
print "do you like me %s %s?" % (first_name, last_name)
likes = raw_input(answer)

print "Where do you live %s %s?" % (first_name, last_name)
lives = raw_input(answer)

print "What kind of computer do you have?"
computer = raw_input(answer)

print """
Alright, so you said %r about like me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)