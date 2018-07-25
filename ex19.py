#defines the functions name and the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
#assings values to the arguments	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

#makes the arguments variables and assigns them values
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#does math
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

#uses variables and math together
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

