#Simple prime number generator function 
def primes():
    start = int(input("Enter the starting number: "))   #input integer value for starting limit
    end = int(input("Enter the ending number: "))       #input integer value for ending limit
    print(f" Prime numbers within {start} and  {end} are : ")   #printing prime numbers within those limits
    for i in range(start, end+1):                       #checking for prime inclusive within the range 
        if i>1:
            for j in range(2,i):                        #starting from least prime no. i.e. 2 to the end of range
                if(i % j==0):                           #if i is completely divisble by j, it's non prime
                    break                               #break the loop
            else:                                       #otherwise print i which is a prime number
                 print(i, end=" ")
               
print(primes())                                         #calling the primes() funtion
