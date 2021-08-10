def checkPrime(start, end):						                      # function to check prime numbers within a range 
	numbers = list(range(start, end+1))			                  # converting range of numbers to a list 
	if start <= 1:								                            # if the starting number is less than or equal to 1
	    numbers.remove(start)					                        # then remove it from list as it is not prime
	for i in range(2,int(end**0.5)+1): 		  	                # iterate through the loop i in range of 2 to (square-root of ending number + 1)
		for j in range (i*i, end+1, i): 		                    # iterate the inner loop j in range of i*i to (ending number + 1) and step i 
			if j in numbers:					                            # if j is the square of i and is completely divisible by i  				
				numbers.remove(j) 				                          # then remove j from the list
	return numbers 								                            # return the list of prime numbers
start = int(input("Enter the starting number "))
end = int(input("Enter the ending number "))
prime = checkPrime(start, end) 					                    # calling checkPrime function 
print(f" Prime numbers between {start} to {end} are : ") 
print(*prime)
