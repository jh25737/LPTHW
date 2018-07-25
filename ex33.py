numbers = []

def adding_numbers (i, numbers):
    print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
    
    
while i < 6:
		print "At the top i is %d" % i
		numbers.append(i)
		i += 1
        adding_numbers(0, numbers)
    
		
	
 print "The numbers: "

 for num in numbers:
        print num



