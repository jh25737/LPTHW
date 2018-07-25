from sys import argv

script, input_file = argv
#defines print_all which reads and prints all the lines
def print_all(f):
	print f.read()
	
#defines rewind funciton, which sets the current line to 0	
def rewind(f):
	f.seek(0)
	
#defines the print line function, which prints the linenumber and current line	
def print_a_line(line_count, f):
	print line_count, f.readline()

#sets and opens the input file selected in argv	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"
#pritns one line at a time
current_line = 1
print_a_line(current_line,current_file)

current_line +=1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)